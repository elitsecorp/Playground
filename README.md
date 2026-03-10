# Ethiopian Market Intelligence Draft

Draft Flask + SQLite application for tracking Ethiopian companies, assets, source evidence, and investment scoring.

## Features

- Company database with sector and industry classification
- Asset database with transaction costs and purchase procedures
- Source evidence registry for auditability
- Five-lens scoring model with automatic total and rating
- Basic industry and financial analysis notes
- Draft ingestion command structure for future web automation

## Quick start

1. Create a virtual environment if desired.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open `http://127.0.0.1:5000`
\n## Static site export (Vercel-friendly)\n\n1. Export the current dataset for the static front end:\n\n`ash\npython export_data.py --out frontend/data/banks.json\n`\n\n2. Deploy the rontend/ directory as a static site on Vercel (set rontend/ as the project root). index.html pulls data/banks.json, so every new export automatically refreshes the hosted listing.\n\n3. Keep using the Flask app locally for manual entry/scoring, rerun the export script before pushing to Vercel to keep the hosted copy in sync.\n
\n## Static site export (Vercel-friendly)\n\n1. Export the current dataset for the static front end:\n\n`ash\npython export_data.py --out frontend/data/banks.json\n`\n\n2. Deploy the rontend/ directory as a static site on Vercel (set rontend/ as the project root). index.html reads data/banks.json, so each export repopulates the hosted listing.\n\n3. Filters allow you to pick an industry, require a minimum score, sort by score/P/E/price/target, and search names/notes/contact details before you dig deeper.\n
