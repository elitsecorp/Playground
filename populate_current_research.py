import sqlite3
from pathlib import Path

DB_PATH = Path("instance/market_intelligence.sqlite3")

COMPANIES = [
    {
        "name": "Wegagen Bank Share Company",
        "sector": "Financial Services",
        "industry": "Banking & Financial Services",
        "ownership_type": "Private",
        "regulator": "National Bank of Ethiopia / Ethiopian Securities Exchange",
        "website": "https://www.wegagen.com",
        "status": "Listed on ESX",
        "industry_analysis": "Banking is one of the first sectors to reach Ethiopia's formal public market. Regulation, deposit franchise economics, and branch-driven customer acquisition create high barriers to entry, while market liberalization and digital payments reforms continue to deepen the sector.",
        "financial_analysis": "Wegagen is already on the ESX Main Market, which improves disclosure relative to most Ethiopian issuers. Financial assessment should still lean on the posted annual and interim reports because live market-price depth remains limited in the early ESX period.",
        "scores": {
            "economy_score": 2,
            "industry_score": 2,
            "business_strength_score": 2,
            "financial_health_score": 1,
            "valuation_score": 1,
            "economy_notes": "Banking benefits from formalization, population growth, and payments-market reform.",
            "industry_notes": "The sector is tightly regulated and difficult to enter at scale.",
            "business_notes": "Long operating history, national footprint, and public-market readiness strengthen competitive position.",
            "financial_notes": "Disclosure quality is stronger because ESX filings are available, but this draft does not yet parse the full statements.",
            "valuation_notes": "Listed status improves price discovery, though trading history is still shallow in the young market.",
            "confidence": "High"
        },
        "assets": [
            {
                "name": "Wegagen Bank ordinary shares (WGBX)",
                "asset_type": "Listed Equity",
                "market": "ESX Main Market",
                "transaction_costs": "Use a licensed ESX trading member. Costs will typically include brokerage/intermediation fees and any exchange or custody charges applied by the intermediary.",
                "purchase_procedure": "Open an investment account through an approved ESX intermediary, complete KYC, fund the account, and place an order for WGBX once market access is available.",
                "eligibility_requirements": "Investor account, KYC, and access through an authorized market intermediary.",
                "currency": "ETB",
                "status": "Active"
            }
        ],
        "sources": [
            {
                "source_type": "Official Exchange Listing",
                "title": "ESX profile for Wegagen Bank Share Company",
                "url": "https://esx.et/directory/wegagen-bank-share-company/",
                "source_date": "2026-03-10",
                "excerpt": "ESX lists Wegagen Bank as WGBX on the Main Market with listing date January 10, 2025.",
                "reliability": "High"
            },
            {
                "source_type": "Official Exchange Listing",
                "title": "ESX listed companies page",
                "url": "https://esx.et/equity-market/listed-companies/",
                "source_date": "2026-03-10",
                "excerpt": "Listed capital, listed shares, number of shareholders, and business classification are published on the ESX listed companies page.",
                "reliability": "High"
            }
        ]
    },
    {
        "name": "Gadaa Bank Share Company",
        "sector": "Financial Services",
        "industry": "Banking & Financial Services",
        "ownership_type": "Private",
        "regulator": "National Bank of Ethiopia / Ethiopian Securities Exchange",
        "website": "https://gadaabank.com.et",
        "status": "Listed on ESX",
        "industry_analysis": "Newer Ethiopian banks can now reach capital markets much earlier in their lifecycle than before, which is meaningful for sector development. Competition among banks is intense, but public listing can improve governance, capital access, and investor visibility.",
        "financial_analysis": "Gadaa has a much shorter operating history than older peers, so financial quality needs to be read with more caution. Its completed ESX listing and available prospectus improve transparency, but the shorter track record argues for a more moderate business and financial score than the oldest listed banks.",
        "scores": {
            "economy_score": 2,
            "industry_score": 2,
            "business_strength_score": 1,
            "financial_health_score": 1,
            "valuation_score": 1,
            "economy_notes": "Sector demand remains supported by financial inclusion and macro reform.",
            "industry_notes": "Banking remains one of the strongest early capital-market sectors in Ethiopia.",
            "business_notes": "The bank has momentum and public-market readiness, but a shorter operating history than larger incumbents.",
            "financial_notes": "Public filings exist, though the operating record is still relatively short.",
            "valuation_notes": "Listed status helps, but early-stage price discovery remains limited.",
            "confidence": "High"
        },
        "assets": [
            {
                "name": "Gadaa Bank ordinary shares (GDAB)",
                "asset_type": "Listed Equity",
                "market": "ESX Main Market",
                "transaction_costs": "Expected to run through licensed intermediaries with brokerage, exchange, and custody-related charges depending on the provider.",
                "purchase_procedure": "Open an investment account with an approved ESX trading member, complete KYC, deposit funds, and submit an order for GDAB.",
                "eligibility_requirements": "Investor account and intermediary onboarding requirements.",
                "currency": "ETB",
                "status": "Active"
            }
        ],
        "sources": [
            {
                "source_type": "Official Exchange Listing",
                "title": "ESX profile for Gadaa Bank Share Company",
                "url": "https://esx.et/directory/gadaa-bank-share-company/",
                "source_date": "2026-03-10",
                "excerpt": "ESX lists Gadaa Bank as GDAB with listing date June 13, 2025 and Main Market classification.",
                "reliability": "High"
            },
            {
                "source_type": "Official Exchange News",
                "title": "ESX announcement on Gadaa Bank listing",
                "url": "https://esx.et/gadaa-bank-s-c-officially-listed-on-the-ethiopian-securities-exchange/",
                "source_date": "2026-03-10",
                "excerpt": "ESX states Gadaa Bank became the second bank listed on the exchange after ECMA prospectus approval in June 2025.",
                "reliability": "High"
            },
            {
                "source_type": "Official Regulator Directory",
                "title": "NBE banks directory entry for Gadaa Bank",
                "url": "https://nbe.gov.et/financial-institutions/banks/",
                "source_date": "2026-03-10",
                "excerpt": "NBE includes Gadaa Bank in its official banks directory, confirming establishment and institution status.",
                "reliability": "High"
            }
        ]
    },
    {
        "name": "Dashen Bank Share Company",
        "sector": "Financial Services",
        "industry": "Banking & Financial Services",
        "ownership_type": "Private",
        "regulator": "National Bank of Ethiopia / Ethiopian Securities Exchange",
        "website": "https://dashenbanksc.com",
        "status": "Registration complete; planned ESX listing",
        "industry_analysis": "Private banks with strong deposit franchises and recognizable brands are likely to be among the deeper pools of future Ethiopian public issuers. The sector remains competitive, but listing progress is concentrated among stronger institutions with governance and scale.",
        "financial_analysis": "Dashen appears to be further along than most private issuers because ESX publicly confirmed completion of its registration process and approval in principle toward listing. Until the final listing is complete and more filing history is available, valuation and liquidity should still be treated as provisional.",
        "scores": {
            "economy_score": 2,
            "industry_score": 2,
            "business_strength_score": 2,
            "financial_health_score": 1,
            "valuation_score": 1,
            "economy_notes": "Banking remains one of the clearest beneficiaries of Ethiopia's financial-sector reform agenda.",
            "industry_notes": "Strong barriers to entry and regulatory oversight support sector quality.",
            "business_notes": "Dashen has a strong brand and is one of the more advanced banks in moving toward formal listing.",
            "financial_notes": "Financial strength looks investable, but this draft still awaits deeper statement extraction.",
            "valuation_notes": "No completed public trading record was verified in this pass, so valuation remains provisional.",
            "confidence": "Medium"
        },
        "assets": [
            {
                "name": "Dashen Bank shareholding interest",
                "asset_type": "Planned Listed Equity / Pre-listing Share",
                "market": "Pre-listing / pending ESX Main Board",
                "transaction_costs": "Current costs depend on issuer-approved transfer mechanics, documentation, and any intermediary charges. Public-market fees should become clearer after final listing.",
                "purchase_procedure": "Before listing, investors should verify transferability and issuer procedures. After listing, purchase should move to approved ESX intermediaries and standard investor-account workflows.",
                "eligibility_requirements": "Depends on current transfer rules before listing and standard KYC after listing.",
                "currency": "ETB",
                "status": "Research"
            }
        ],
        "sources": [
            {
                "source_type": "Official Exchange News",
                "title": "ESX welcomes Dashen Bank's progress toward planned listing",
                "url": "https://esx.et/esx-welcomes-dashen-banks-progress-toward-planned-listing/",
                "source_date": "2026-03-10",
                "excerpt": "ESX says Dashen completed its registration process and received approval in principle toward listing, subject to remaining requirements.",
                "reliability": "High"
            },
            {
                "source_type": "Official Website",
                "title": "Dashen Bank official website",
                "url": "https://dashenbanksc.com/",
                "source_date": "2026-03-10",
                "excerpt": "Used for issuer identity and institutional reference.",
                "reliability": "High"
            }
        ]
    },
    {
        "name": "Ethio Telecom Share Company",
        "sector": "Telecom Services",
        "industry": "Telecommunications",
        "ownership_type": "State-Controlled",
        "regulator": "Ethiopian Communications Authority / Ethiopian Securities Exchange",
        "website": "https://www.ethiotelecom.et",
        "status": "Listed on ESX",
        "industry_analysis": "Telecommunications is strategically important infrastructure with high barriers to entry, sticky demand, and upside from data, infrastructure sharing, and mobile financial services. In Ethiopia, the sector also benefits from policy focus on digital adoption and national connectivity.",
        "financial_analysis": "Ethio Telecom's ESX listing and published historical financial information materially improve visibility compared with most Ethiopian corporates. Even so, valuation work should be treated carefully until deeper live market data and a longer public-market history are available.",
        "scores": {
            "economy_score": 2,
            "industry_score": 2,
            "business_strength_score": 2,
            "financial_health_score": 1,
            "valuation_score": 1,
            "economy_notes": "Digitalization and mobile-money adoption are strong macro tailwinds.",
            "industry_notes": "Telecom has very high barriers to entry and strategic national importance.",
            "business_notes": "Ethio Telecom has brand scale, infrastructure control, and service breadth.",
            "financial_notes": "Historical financial data is available through ESX, but this draft has not yet parsed all metrics into structured ratios.",
            "valuation_notes": "Listed status improves access to price discovery, but the market is still early-stage.",
            "confidence": "High"
        },
        "assets": [
            {
                "name": "Ethio Telecom ordinary shares (TELE)",
                "asset_type": "Listed Equity",
                "market": "ESX Main Market",
                "transaction_costs": "Buying requires an approved intermediary and will generally involve brokerage or service fees plus any account or custody charges.",
                "purchase_procedure": "Open an investment account through a licensed ESX intermediary, complete KYC, fund the account, and place an order for TELE.",
                "eligibility_requirements": "Investor account and intermediary onboarding requirements.",
                "currency": "ETB",
                "status": "Active"
            }
        ],
        "sources": [
            {
                "source_type": "Official Exchange Listing",
                "title": "ESX profile for Ethio Telecom Share Company",
                "url": "https://esx.et/directory/ethio-telecom-share-company/",
                "source_date": "2026-03-10",
                "excerpt": "ESX lists Ethio Telecom as TELE with listing date June 25, 2025.",
                "reliability": "High"
            },
            {
                "source_type": "Official Exchange Listing",
                "title": "ESX listed companies page for Ethio Telecom",
                "url": "https://esx.et/equity-market/listed-companies/",
                "source_date": "2026-03-10",
                "excerpt": "ESX publishes listed capital, share count, shareholder count, and prospectus links for Ethio Telecom.",
                "reliability": "High"
            },
            {
                "source_type": "Official Website",
                "title": "Ethio Telecom annual financial statement page",
                "url": "https://www.ethiotelecom.et/annual-financial-statement/",
                "source_date": "2026-03-10",
                "excerpt": "Ethio Telecom publishes annual audit reports and financial statements on its official site.",
                "reliability": "High"
            }
        ]
    },
    {
        "name": "Zemen Insurance S.C.",
        "sector": "Financial Services",
        "industry": "Insurance",
        "ownership_type": "Private",
        "regulator": "National Bank of Ethiopia",
        "website": "https://zemeninsurance.com/",
        "status": "Private / potential future market candidate",
        "industry_analysis": "Insurance is still earlier than banking in Ethiopia's public-market development, but the sector is institutionally important and increasingly visible to ESX as a future issuer and investor base. Competitive intensity is meaningful, yet regulatory licensing and capital requirements still provide barriers to entry.",
        "financial_analysis": "Zemen is a relatively young insurer, and public market data is limited. Its official site provides establishment history, branch growth, and high-level balance sheet figures, which supports a cautious but positive early assessment rather than a high-conviction score.",
        "scores": {
            "economy_score": 1,
            "industry_score": 1,
            "business_strength_score": 1,
            "financial_health_score": 1,
            "valuation_score": 0,
            "economy_notes": "Insurance should benefit from long-term financial deepening, but current market depth is still developing.",
            "industry_notes": "The industry has barriers to entry but is less mature in public-market access than banking.",
            "business_notes": "Zemen has grown branch count quickly for a younger insurer.",
            "financial_notes": "Official site disclosures show assets and capital growth, but structured public financial history remains limited.",
            "valuation_notes": "No verified public market price was found in this pass.",
            "confidence": "Medium"
        },
        "assets": [
            {
                "name": "Zemen Insurance shareholding interest",
                "asset_type": "Private Share / OTC-style transfer",
                "market": "Private transfer",
                "transaction_costs": "Costs depend on transfer approval, legal documentation, and any intermediary support used for private transactions.",
                "purchase_procedure": "Verify whether shares are transferable, confirm company register or certificate evidence, complete KYC and transfer documentation, and follow company-approved procedures.",
                "eligibility_requirements": "Buyer identity and company approval requirements may apply.",
                "currency": "ETB",
                "status": "Research"
            }
        ],
        "sources": [
            {
                "source_type": "Official Regulator Directory",
                "title": "NBE insurers directory entry for Zemen Insurance",
                "url": "https://nbe.gov.et/financial-institutions/insurers/",
                "source_date": "2026-03-10",
                "excerpt": "NBE lists Zemen Insurance as an established licensed insurer.",
                "reliability": "High"
            },
            {
                "source_type": "Official Website",
                "title": "Zemen Insurance about page",
                "url": "https://zemeninsurance.com/about-us/",
                "source_date": "2026-03-10",
                "excerpt": "The company states it was established in 2020 and reports assets, paid-up capital, and branch expansion details.",
                "reliability": "High"
            }
        ]
    },
    {
        "name": "Bunna Insurance S.C.",
        "sector": "Financial Services",
        "industry": "Insurance",
        "ownership_type": "Private",
        "regulator": "National Bank of Ethiopia",
        "website": "https://bunnainsurance.com/",
        "status": "Private / potential future market candidate",
        "industry_analysis": "Insurance remains one of the next likely sectors for Ethiopia's capital market broadening, especially as ESX has been actively engaging insurers in 2026. Firms with recurring underwriting operations and investable balance sheets could become future listings or institutional market participants.",
        "financial_analysis": "Bunna provides annual reports on its official site, which is useful for future structured extraction. In this draft pass, the existence of current annual reports and its regulated status support inclusion, but valuation remains unverified because no public trading venue was confirmed.",
        "scores": {
            "economy_score": 1,
            "industry_score": 1,
            "business_strength_score": 1,
            "financial_health_score": 1,
            "valuation_score": 0,
            "economy_notes": "Macro financial deepening supports the insurance opportunity set, though the market is less advanced than banking.",
            "industry_notes": "Insurance has structural importance but public-market access is still emerging.",
            "business_notes": "The company is established and appears to maintain regular reporting.",
            "financial_notes": "Annual reports exist on the official website, but deeper ratio analysis is still pending.",
            "valuation_notes": "No verified public market price was found in this pass.",
            "confidence": "Medium"
        },
        "assets": [
            {
                "name": "Bunna Insurance shareholding interest",
                "asset_type": "Private Share / OTC-style transfer",
                "market": "Private transfer",
                "transaction_costs": "Likely to include transfer documentation, approval steps, and any legal or intermediary fees involved in private transactions.",
                "purchase_procedure": "Confirm transferability with the company, verify shareholder documentation, and process the transfer under company and legal requirements.",
                "eligibility_requirements": "Buyer identity and transfer approvals may apply.",
                "currency": "ETB",
                "status": "Research"
            }
        ],
        "sources": [
            {
                "source_type": "Official Regulator Directory",
                "title": "NBE insurers directory entry for Bunna Insurance",
                "url": "https://nbe.gov.et/financial-institutions/insurers/",
                "source_date": "2026-03-10",
                "excerpt": "NBE lists Bunna Insurance as an established insurer.",
                "reliability": "High"
            },
            {
                "source_type": "Official Website",
                "title": "Bunna Insurance publication page",
                "url": "https://bunnainsurance.com/Home/Publication",
                "source_date": "2026-03-10",
                "excerpt": "Bunna Insurance publishes annual reports for 2024-2025 and earlier years on its official site.",
                "reliability": "High"
            },
            {
                "source_type": "Official Exchange News",
                "title": "ESX insurance information session",
                "url": "https://esx.et/",
                "source_date": "2026-03-10",
                "excerpt": "ESX reported on March 9, 2026 that it held an information session with insurance companies on listing and OTC opportunities.",
                "reliability": "High"
            }
        ]
    }
]


def ensure_db():
    if DB_PATH.exists():
        return
    raise SystemExit("Database not found. Run the Flask app once or visit /setup first.")


def upsert_company(db, company):
    existing = db.execute("SELECT id FROM companies WHERE name = ?", (company["name"],)).fetchone()
    if existing:
        company_id = existing[0]
        db.execute(
            """
            UPDATE companies
            SET sector = ?, industry = ?, ownership_type = ?, regulator = ?, website = ?,
                status = ?, industry_analysis = ?, financial_analysis = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (
                company["sector"], company["industry"], company["ownership_type"], company["regulator"],
                company["website"], company["status"], company["industry_analysis"], company["financial_analysis"], company_id,
            ),
        )
    else:
        cur = db.execute(
            """
            INSERT INTO companies (
                name, sector, industry, ownership_type, regulator, website, status, industry_analysis, financial_analysis
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                company["name"], company["sector"], company["industry"], company["ownership_type"], company["regulator"],
                company["website"], company["status"], company["industry_analysis"], company["financial_analysis"],
            ),
        )
        company_id = cur.lastrowid

    score = company["scores"]
    total = sum(score[k] for k in ["economy_score", "industry_score", "business_strength_score", "financial_health_score", "valuation_score"])
    rating = "Strong" if total >= 9 else "Good" if total >= 7 else "Moderate" if total >= 5 else "Avoid"
    score_exists = db.execute("SELECT id FROM scores WHERE company_id = ?", (company_id,)).fetchone()
    score_params = (
        score["economy_score"], score["industry_score"], score["business_strength_score"],
        score["financial_health_score"], score["valuation_score"], total, rating,
        score["economy_notes"], score["industry_notes"], score["business_notes"], score["financial_notes"],
        score["valuation_notes"], score["confidence"], company_id,
    )
    if score_exists:
        db.execute(
            """
            UPDATE scores
            SET economy_score = ?, industry_score = ?, business_strength_score = ?, financial_health_score = ?,
                valuation_score = ?, total_score = ?, rating = ?, economy_notes = ?, industry_notes = ?,
                business_notes = ?, financial_notes = ?, valuation_notes = ?, confidence = ?, updated_at = CURRENT_TIMESTAMP
            WHERE company_id = ?
            """,
            score_params,
        )
    else:
        db.execute(
            """
            INSERT INTO scores (
                economy_score, industry_score, business_strength_score, financial_health_score, valuation_score,
                total_score, rating, economy_notes, industry_notes, business_notes, financial_notes,
                valuation_notes, confidence, company_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            score_params,
        )

    db.execute("DELETE FROM assets WHERE company_id = ?", (company_id,))
    for asset in company["assets"]:
        db.execute(
            """
            INSERT INTO assets (
                company_id, name, asset_type, market, transaction_costs, purchase_procedure,
                eligibility_requirements, currency, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                company_id, asset["name"], asset["asset_type"], asset["market"], asset["transaction_costs"],
                asset["purchase_procedure"], asset["eligibility_requirements"], asset["currency"], asset["status"],
            ),
        )

    db.execute("DELETE FROM sources WHERE company_id = ?", (company_id,))
    for source in company["sources"]:
        db.execute(
            """
            INSERT INTO sources (
                company_id, source_type, title, url, source_date, excerpt, reliability
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                company_id, source["source_type"], source["title"], source["url"], source["source_date"],
                source["excerpt"], source["reliability"],
            ),
        )


def main():
    ensure_db()
    db = sqlite3.connect(DB_PATH)
    for company in COMPANIES:
        upsert_company(db, company)
    db.commit()
    db.close()
    print(f"Upserted {len(COMPANIES)} companies into {DB_PATH}.")


if __name__ == "__main__":
    main()
