import argparse
import json
import sqlite3
from pathlib import Path
from typing import Iterable


def normalize_row(row):
    return {key: row[key] for key in row.keys()}


def fetch_assets(conn, company_id: int) -> Iterable[dict]:
    rows = conn.execute(
        "SELECT name, asset_type, market, transaction_costs, purchase_procedure, eligibility_requirements, currency, status FROM assets WHERE company_id = ?",
        (company_id,),
    ).fetchall()
    for row in rows:
        yield normalize_row(row)


def fetch_sources(conn, company_id: int) -> Iterable[dict]:
    rows = conn.execute(
        "SELECT source_type, title, url, source_date, excerpt, reliability FROM sources WHERE company_id = ? ORDER BY source_date DESC",
        (company_id,),
    ).fetchall()
    for row in rows:
        yield normalize_row(row)


def export(db_path: Path, out_path: Path) -> None:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        """
        SELECT
            c.id,
            c.name,
            c.sector,
            c.industry,
            c.ownership_type,
            c.regulator,
            c.website,
            c.status,
            c.industry_analysis,
            c.financial_analysis,
            c.contact_phone,
            c.contact_email,
            c.contact_address,
            c.investor_notes,
            s.total_score,
            s.rating,
            s.economy_score,
            s.industry_score,
            s.business_strength_score,
            s.financial_health_score,
            s.valuation_score,
            s.eps,
            s.implied_pe,
            s.current_price,
            s.target_price_for_20pc
        FROM companies c
        LEFT JOIN scores s ON s.company_id = c.id
        ORDER BY s.total_score DESC, c.name ASC
        """
    )

    banks = []
    for row in rows:
        company_id = row["id"]
        bank = dict(row)
        bank["assets"] = list(fetch_assets(conn, company_id))
        bank["sources"] = list(fetch_sources(conn, company_id))
        bank["target_price_for_20pc"] = float(row["target_price_for_20pc"] or 0)
        bank["current_price"] = float(row["current_price"] or 0)
        bank["implied_pe"] = float(row["implied_pe"] or 0)
        bank["eps"] = float(row["eps"] or 0)
        bank["price_notes"] = (
            f"Target price for 20% yield: {bank['target_price_for_20pc']:.2f} ETB"
            if bank["target_price_for_20pc"]
            else "EPS or price missing"
        )
        banks.append(bank)

    conn.close()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(banks, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Export bank data to JSON for static hosting.")
    parser.add_argument(
        "--db",
        type=Path,
        default=Path("instance/market_intelligence.sqlite3"),
        help="Path to the SQLite database.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("frontend/data/banks.json"),
        help="Output JSON path consumed by the static site.",
    )
    args = parser.parse_args()
    export(args.db, args.out)
    print(f"Exported {args.out}")


if __name__ == "__main__":
    main()
