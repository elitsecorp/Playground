from .db import get_db
from .scoring import normalize_scores


def parse_float(value):
    try:
        if value is None or value == "":
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def dashboard_summary():
    db = get_db()
    summary = db.execute(
        """
        SELECT
            (SELECT COUNT(*) FROM companies) AS companies,
            (SELECT COUNT(*) FROM assets) AS assets,
            (SELECT COUNT(*) FROM sources) AS sources,
            (SELECT COUNT(*) FROM scores) AS scores
        """
    ).fetchone()
    top_companies = db.execute(
        """
        SELECT c.id, c.name, c.industry, s.total_score, s.rating
        FROM companies c
        LEFT JOIN scores s ON s.company_id = c.id
        ORDER BY s.total_score DESC, c.name ASC
        LIMIT 8
        """
    ).fetchall()
    return summary, top_companies


def list_companies():
    db = get_db()
    return db.execute(
        """
        SELECT c.*, s.economy_score, s.industry_score, s.business_strength_score,
               s.financial_health_score, s.valuation_score, s.total_score, s.rating
        FROM companies c
        LEFT JOIN scores s ON s.company_id = c.id
        ORDER BY c.name ASC
        """
    ).fetchall()


def company_detail(company_id):
    db = get_db()
    company = db.execute(
        """
        SELECT c.*, s.economy_score, s.industry_score, s.business_strength_score,
               s.financial_health_score, s.valuation_score, s.total_score, s.rating,
               s.economy_notes, s.industry_notes, s.business_notes,
               s.financial_notes, s.valuation_notes, s.confidence, s.eps,
               s.implied_pe, s.current_price, s.target_price_for_20pc
        FROM companies c
        LEFT JOIN scores s ON s.company_id = c.id
        WHERE c.id = ?
        """,
        (company_id,),
    ).fetchone()
    assets = db.execute(
        """
        SELECT *
        FROM assets
        WHERE company_id = ?
        ORDER BY asset_type, name
        """,
        (company_id,),
    ).fetchall()
    sources = db.execute(
        """
        SELECT *
        FROM sources
        WHERE company_id = ?
        ORDER BY source_date DESC, created_at DESC
        """,
        (company_id,),
    ).fetchall()
    return company, assets, sources


def create_company(payload):
    db = get_db()
    cursor = db.execute(
        """
        INSERT INTO companies (
            name, sector, industry, ownership_type, regulator,
            website, status, industry_analysis, financial_analysis,
            contact_phone, contact_email, contact_address, investor_notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            payload["name"],
            payload.get("sector", ""),
            payload.get("industry", ""),
            payload.get("ownership_type", ""),
            payload.get("regulator", ""),
            payload.get("website", ""),
            payload.get("status", "Research"),
            payload.get("industry_analysis", ""),
            payload.get("financial_analysis", ""),
            payload.get("contact_phone", ""),
            payload.get("contact_email", ""),
            payload.get("contact_address", ""),
            payload.get("investor_notes", ""),
        ),
    )
    company_id = cursor.lastrowid
    upsert_score(company_id, payload)
    db.commit()
    return company_id


def score_metrics(payload):
    eps = parse_float(payload.get("eps"))
    current_price = parse_float(payload.get("current_price"))
    implied_pe = parse_float(payload.get("implied_pe"))
    if implied_pe is None and current_price and eps:
        implied_pe = current_price / eps if eps else None
    target_price = parse_float(payload.get("target_price_for_20pc"))
    if target_price is None and eps:
        target_price = eps / 0.2 if eps else None
    return {
        "eps": eps or 0,
        "implied_pe": implied_pe or 0,
        "current_price": current_price or 0,
        "target_price_for_20pc": target_price or 0,
    }


def upsert_score(company_id, payload):
    db = get_db()
    scores = normalize_scores(payload)
    metric = score_metrics(payload)
    existing = db.execute(
        "SELECT id FROM scores WHERE company_id = ?",
        (company_id,),
    ).fetchone()
    params = (
        company_id,
        scores["economy_score"],
        scores["industry_score"],
        scores["business_strength_score"],
        scores["financial_health_score"],
        scores["valuation_score"],
        scores["total_score"],
        scores["rating"],
        payload.get("economy_notes", ""),
        payload.get("industry_notes", ""),
        payload.get("business_notes", ""),
        payload.get("financial_notes", ""),
        payload.get("valuation_notes", ""),
        payload.get("confidence", "Medium"),
        metric["eps"],
        metric["implied_pe"],
        metric["current_price"],
        metric["target_price_for_20pc"],
    )
    if existing:
        db.execute(
            """
            UPDATE scores
            SET economy_score = ?, industry_score = ?, business_strength_score = ?,
                financial_health_score = ?, valuation_score = ?, total_score = ?,
                rating = ?, economy_notes = ?, industry_notes = ?, business_notes = ?,
                financial_notes = ?, valuation_notes = ?, confidence = ?,
                eps = ?, implied_pe = ?, current_price = ?, target_price_for_20pc = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE company_id = ?
            """,
            params[1:] + (company_id,),
        )
    else:
        db.execute(
            """
            INSERT INTO scores (
                company_id, economy_score, industry_score, business_strength_score,
                financial_health_score, valuation_score, total_score, rating,
                economy_notes, industry_notes, business_notes, financial_notes,
                valuation_notes, confidence, eps, implied_pe, current_price,
                target_price_for_20pc
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            params,
        )


def create_asset(company_id, payload):
    db = get_db()
    db.execute(
        """
        INSERT INTO assets (
            company_id, name, asset_type, market, transaction_costs,
            purchase_procedure, eligibility_requirements, currency, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            company_id,
            payload["name"],
            payload.get("asset_type", ""),
            payload.get("market", ""),
            payload.get("transaction_costs", ""),
            payload.get("purchase_procedure", ""),
            payload.get("eligibility_requirements", ""),
            payload.get("currency", "ETB"),
            payload.get("status", "Research"),
        ),
    )
    db.commit()


def add_source(company_id, payload):
    db = get_db()
    db.execute(
        """
        INSERT INTO sources (
            company_id, source_type, title, url, source_date, excerpt, reliability
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            company_id,
            payload.get("source_type", "Website"),
            payload["title"],
            payload.get("url", ""),
            payload.get("source_date"),
            payload.get("excerpt", ""),
            payload.get("reliability", "Medium"),
        ),
    )
    db.commit()
