import argparse
import sqlite3
from pathlib import Path


OFFICIAL_SOURCES = [
    {
        "name": "National Bank of Ethiopia",
        "category": "Regulator",
        "url": "https://nbe.gov.et/",
        "notes": "Use for regulated financial institutions and official directories.",
    },
    {
        "name": "Ethiopian Securities Exchange",
        "category": "Exchange",
        "url": "https://esx.et/",
        "notes": "Use for listed issuers and exchange market structure.",
    },
    {
        "name": "Ethiopian Investment Commission",
        "category": "Investment",
        "url": "https://investethiopia.gov.et/",
        "notes": "Use for sector and investment ecosystem references.",
    },
]


def db_path():
    return Path("instance/market_intelligence.sqlite3")


def ensure_seed_sources():
    path = db_path()
    if not path.exists():
        print("Database not found. Run the Flask app and visit /setup or run flask init-db first.")
        return

    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    companies = db.execute("SELECT id, name FROM companies").fetchall()
    for company in companies:
        for source in OFFICIAL_SOURCES:
            title = f"{source['name']} reference for {company['name']}"
            exists = db.execute(
                "SELECT 1 FROM sources WHERE company_id = ? AND title = ?",
                (company["id"], title),
            ).fetchone()
            if exists:
                continue
            db.execute(
                """
                INSERT INTO sources (
                    company_id, source_type, title, url, source_date, excerpt, reliability
                ) VALUES (?, ?, ?, ?, date('now'), ?, ?)
                """,
                (
                    company["id"],
                    source["category"],
                    title,
                    source["url"],
                    source["notes"],
                    "Medium",
                ),
            )
    db.commit()
    db.close()
    print("Seeded source placeholders for tracked companies.")


def main():
    parser = argparse.ArgumentParser(description="Draft ingestion pipeline for Ethiopian market intelligence.")
    parser.add_argument(
        "--seed-only",
        action="store_true",
        help="Populate draft source placeholders without fetching live web data.",
    )
    args = parser.parse_args()

    if args.seed_only:
        ensure_seed_sources()
        return

    print("Live web ingestion is not wired yet in this draft.")
    print("Next step: add fetchers that collect source text, then run extraction and scoring.")


if __name__ == "__main__":
    main()
