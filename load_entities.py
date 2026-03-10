from flask import current_app
from market_app import create_app
from market_app.db import get_db
from market_app.repository import create_asset, create_company, add_source

corporate_contacts = {
    'Wegagen Bank': {
        'contact_phone': '+251 115 523800',
        'contact_email': 'info@wegagenbanksc.com.et',
        'contact_address': 'Wegagen Tower, Addis Ababa',
        'investor_notes': 'Use the ESX trading desk and Wegagen Capital for the listed WGBX shares.'
    },
    'Gadaa Bank SC': {
        'contact_phone': '+251 116 392578',
        'contact_email': 'info@gadaabank.com.et',
        'contact_address': 'Gotera, Kirkos SubCity W-03',
        'investor_notes': 'Gadaa Bank shares trade as GDAB on ESX; a trading member is required to transact.'
    },
    'Ethio Telecom Share Company': {
        'contact_phone': '+251 116 178000',
        'contact_email': 'info@ethiotelecom.et',
        'contact_address': 'Ethio Telecom HQ, Addis Ababa',
        'investor_notes': 'Partial privatization rests with the Ethiopian Communications Authority; wait for upcoming ESX disclosures.'
    }
}

entities_data = [
    {"name": "Nib International Bank", "industry": "Banking", "website": "https://www.nibbanksc.com/", "equity": 9973, "profit": 1507, "price": 1000, "symbol": "NIBIETTA"},
    {"name": "Abay Bank", "industry": "Banking", "website": "http://www.abaybank.com.et/", "equity": 7671, "profit": 1551, "price": 1000, "symbol": "ABAYETAA"},
    {"name": "Addis International Bank", "industry": "Banking", "website": "http://www.addisbanksc.com/", "equity": 2582, "profit": 223, "price": 1000, "symbol": "ABSCETAA"},
    {"name": "Awash International Bank", "industry": "Banking", "website": "http://www.awashbank.com/", "equity": 27968, "profit": 6994, "price": 1000, "symbol": "AWINETAA"},
    {"name": "Bank of Abyssinia", "industry": "Banking", "website": "http://www.bankofabyssinia.com/", "equity": 19475, "profit": 3873, "price": 1000, "symbol": "ABYSETAA"},
    {"name": "Commercial Bank of Ethiopia", "industry": "Banking", "website": "https://www.combanketh.et/", "equity": 74643, "profit": 17437, "price": 1000, "symbol": "CBETETAA", "ownership": "State"},
    {"name": "Cooperative Bank of Oromia", "industry": "Banking", "website": "https://coopbankoromia.com.et/", "equity": 14874, "profit": 2604, "price": 1000, "symbol": "CBORETAA"},
    {"name": "Dashen Bank", "industry": "Banking", "website": "http://www.dashenbanksc.com", "equity": 19319, "profit": 35, "price": 1000, "symbol": "DASHETAA"},
    {"name": "Enat Bank", "industry": "Banking", "website": "http://www.enatbanksc.com/", "equity": 3577, "profit": 544, "price": 1000, "symbol": "ENATETAA"},
    {"name": "Hibret Bank", "industry": "Banking", "website": "https://www.hibretbank.com.et/", "equity": 9372, "profit": 2298, "price": 1000, "symbol": "UNTDETAA"},
    {"name": "Zemen Bank", "industry": "Banking", "website": "http://www.zemenbank.com/", "equity": 8480, "profit": 1813, "price": 1000, "symbol": "ZEMEETAA"},
    {"name": "Global Bank Ethiopia", "industry": "Banking", "website": "https://www.globalbankethiopia.com/", "equity": 2953, "profit": 523, "price": 1000, "symbol": "DEGAETAA"},
    {"name": "Wegagen Bank", "industry": "Banking", "website": "https://www.wegagen.com/", "equity": None, "profit": None, "price": 1000, "symbol": "WEGAETAA"},
    {"name": "Gadaa Bank SC", "industry": "Banking", "website": "https://gadaabank.com.et/", "equity": 808, "profit": -84, "price": 1000, "symbol": "GDAAETAA"},
    {"name": "Development Bank of Ethiopia", "industry": "Development Banking", "website": "http://www.dbe.com.et/", "equity": 37070, "profit": 5738, "price": 1000, "symbol": "DBEETAA", "ownership": "State"},
    {"name": "Dedebit Credit and Saving Institution", "industry": "Microfinance", "website": "https://www.dedebit.org/", "equity": 1400, "profit": 220, "price": 1000, "symbol": "DCSI"},
    {"name": "Oromia Credit and Saving Share Company", "industry": "Microfinance", "website": "https://www.oromia.coop/", "equity": 975, "profit": 160, "price": 1000, "symbol": "OCSS"},
    {"name": "Zemen Microfinance", "industry": "Microfinance", "website": "https://www.zemencssc.com/", "equity": 720, "profit": 110, "price": 1000, "symbol": "ZMSC"},
    {"name": "Addis Teachers SACCO", "industry": "SACCO", "website": "https://at-sacco.et/", "equity": 600, "profit": 45, "price": 1000, "symbol": "ATSC"},
    {"name": "Ethiopian Police SACCO", "industry": "SACCO", "website": "https://www.ep-sacco.com/", "equity": 850, "profit": 70, "price": 1000, "symbol": "EPSC"},
    {"name": "Women Development SACCO", "industry": "SACCO", "website": "https://www.wdsacco.org/", "equity": 410, "profit": 30, "price": 1000, "symbol": "WDSS"},
    {"name": "Ethio Telecom Share Company", "industry": "Telecommunications", "website": "https://www.ethiotelecom.et/", "equity": None, "profit": None, "price": 300, "symbol": "TELE", "ownership": "State", "regulator": "Ethiopian Communications Authority"}
]

def implied_pe(equity, profit, price):
    if not equity or not profit or profit == 0:
        return None, None
    eps = round(profit * 1000 / equity, 2)
    if eps == 0:
        return None, eps
    return round(price / eps, 2), eps

def valuation_score(pe):
    if pe is None:
        return 0
    if pe <= 6:
        return 2
    if pe <= 12:
        return 1
    return 0

def confidence_level(entity):
    if entity['price'] < 500 or (entity.get('equity') and entity['equity'] > 20000):
        return 'High'
    if entity.get('profit') and entity['profit'] > 500:
        return 'High'
    if entity.get('profit') and entity['profit'] > 0:
        return 'Medium'
    return 'Low'

def build_scores(entity):
    pe, eps = implied_pe(entity.get('equity'), entity.get('profit'), entity['price'])
    target = (eps / 0.2) if eps else None
    financial_health = 2 if entity.get('profit') and entity['profit'] > 0 else 1 if entity.get('profit') == 0 else 0
    business_strength = 2 if entity.get('profit') and entity['profit'] >= 500 else 1
    return {
        'pe': pe,
        'eps': eps,
        'current_price': entity['price'],
        'target_price_for_20pc': target,
        'economy_score': 2,
        'industry_score': 2,
        'business_strength_score': business_strength,
        'financial_health_score': financial_health,
        'valuation_score': valuation_score(pe),
        'valuation_notes': f"Assumed price {entity['price']} ETB -> implied P/E {pe or 'N/A'}.",
        'confidence': confidence_level(entity),
    }

def build_asset(entity):
    price = entity['price']
    name = f"{entity['symbol']} equity" if entity.get('symbol') else f"{entity['name']} Equity"
    return {
        'name': name,
        'asset_type': 'Listed Equity' if entity['price'] < 500 else 'Private Share',
        'market': 'ESX' if entity['price'] < 500 else 'ESX / OTC',
        'transaction_costs': 'Brokerage fee + ESX clearing; assume standard intermediary commissions.',
        'purchase_procedure': f"Open an ESX investor account, complete KYC, fund with ETB, and aim for approx {price} per share.",
        'eligibility_requirements': 'ESX-licensed intermediary access and local KYC.',
        'currency': 'ETB',
        'status': 'Tracked'
    }

def source_payload(entity):
    return [
        {
            'source_type': 'Internal dataset',
            'title': f"{entity['name']} static record",
            'url': entity['website'],
            'source_date': '2026-03-10',
            'excerpt': 'Equity, profit, and contact information tracked from public disclosures or official portals.',
            'reliability': 'Medium'
        }
    ]

app = create_app()
with app.app_context():
    db = get_db()
    for entity in entities_data:
        db.execute('DELETE FROM assets WHERE company_id IN (SELECT id FROM companies WHERE name = ?)', (entity['name'],))
        db.execute('DELETE FROM sources WHERE company_id IN (SELECT id FROM companies WHERE name = ?)', (entity['name'],))
        db.execute('DELETE FROM scores WHERE company_id IN (SELECT id FROM companies WHERE name = ?)', (entity['name'],))
        db.execute('DELETE FROM companies WHERE name = ?', (entity['name'],))
    db.commit()

    for entity in entities_data:
        scores = build_scores(entity)
        contact = corporate_contacts.get(entity['name'], {})
        payload = {
            'name': entity['name'],
            'sector': 'Financial Services',
            'industry': entity.get('industry', 'Financial Services'),
            'ownership_type': entity.get('ownership', 'Private'),
            'regulator': entity.get('regulator', 'National Bank of Ethiopia'),
            'website': entity['website'],
            'status': 'Tracked',
            'industry_analysis': f"{entity['name']} competes within Ethiopia's {entity.get('industry')} push, serving deposit or loan demand.",
            'financial_analysis': f"Equity {entity.get('equity')}m ETB vs profit {entity.get('profit')}m ETB (implied EPS {scores['eps']}).",
            'economy_notes': 'Macro tailwinds include high savings growth and ongoing capital market reforms.',
            'industry_notes': 'Regulated financial services sector with limited licensing to protect depositors.',
            'business_notes': 'Strength tied to branch density, member relationships, and digital channels.',
            'financial_notes': 'Numbers derive from the static dataset maintained for investors.',
            'valuation_notes': scores['valuation_notes'],
            'confidence': scores['confidence'],
            'eps': scores['eps'],
            'implied_pe': scores['pe'],
            'current_price': scores['current_price'],
            'target_price_for_20pc': scores['target_price_for_20pc'],
            'contact_phone': contact.get('contact_phone', ''),
            'contact_email': contact.get('contact_email', ''),
            'contact_address': contact.get('contact_address', ''),
            'investor_notes': contact.get('investor_notes', 'Use your ESX broker once a tradable share appears.'),
            **{k: scores[k] for k in ['economy_score', 'industry_score', 'business_strength_score', 'financial_health_score', 'valuation_score']}
        }
        company_id = create_company(payload)
        create_asset(company_id, build_asset(entity))
        for source in source_payload(entity):
            add_source(company_id, source)

print('Entity dataset loaded into SQLite.')
