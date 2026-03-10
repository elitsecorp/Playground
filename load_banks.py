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

banks_data = [
    {"name": "Nib International Bank", "website": "https://www.nibbanksc.com/", "equity": 9973, "profit": 1507, "price": 1000, "symbol": "NIBIETTA"},
    {"name": "Abay Bank", "website": "http://www.abaybank.com.et/", "equity": 7671, "profit": 1551, "price": 1000, "symbol": "ABAYETAA"},
    {"name": "Addis International Bank", "website": "http://www.addisbanksc.com/", "equity": 2582, "profit": 223, "price": 1000, "symbol": "ABSCETAA"},
    {"name": "Amhara Bank", "website": "https://www.amharabank.com.et/", "equity": 5879, "profit": -170, "price": 1000, "symbol": "AMHRETAA"},
    {"name": "Awash International Bank", "website": "http://www.awashbank.com/", "equity": 27968, "profit": 6994, "price": 1000, "symbol": "AWINETAA"},
    {"name": "Bank of Abyssinia", "website": "http://www.bankofabyssinia.com/", "equity": 19475, "profit": 3873, "price": 1000, "symbol": "ABYSETAA"},
    {"name": "Berhan International Bank", "website": "http://berhanbanksc.com/", "equity": 5029, "profit": 509, "price": 1000, "symbol": "BERHETAA"},
    {"name": "Bunna International Bank", "website": "http://www.bunnabanksc.com/", "equity": None, "profit": 949, "price": 1000, "symbol": "BUNAETAA"},
    {"name": "Commercial Bank of Ethiopia", "website": "https://www.combanketh.et/", "equity": 74643, "profit": 17437, "price": 1000, "symbol": "CBETETAA", "ownership": "State"},
    {"name": "Cooperative Bank of Oromia", "website": "https://coopbankoromia.com.et/", "equity": 14874, "profit": 2604, "price": 1000, "symbol": "CBORETAA"},
    {"name": "Dashen Bank", "website": "http://www.dashenbanksc.com", "equity": 19319, "profit": 35, "price": 1000, "symbol": "DASHETAA"},
    {"name": "Global Bank Ethiopia", "website": "https://www.globalbankethiopia.com/", "equity": 2953, "profit": 523, "price": 1000, "symbol": "DEGAETAA"},
    {"name": "Enat Bank", "website": "http://www.enatbanksc.com/", "equity": 3577, "profit": 544, "price": 1000, "symbol": "ENATETAA"},
    {"name": "Lion International Bank", "website": "http://www.anbesabank.com/", "equity": None, "profit": 747, "price": 1000, "symbol": "LIBSETAA"},
    {"name": "Oromia International Bank", "website": "http://www.oromiabank.com/", "equity": 8658, "profit": -417, "price": 1000, "symbol": "ORIRETAA"},
    {"name": "Hibret Bank", "website": "https://www.hibretbank.com.et/", "equity": 9372, "profit": 2298, "price": 1000, "symbol": "UNTDETAA"},
    {"name": "Wegagen Bank", "website": "https://www.wegagen.com/", "equity": None, "profit": None, "price": 1000, "symbol": "WEGAETAA"},
    {"name": "Zemen Bank", "website": "http://www.zemenbank.com/", "equity": 8480, "profit": 1813, "price": 1000, "symbol": "ZEMEETAA"},
    {"name": "Development Bank of Ethiopia", "website": "http://www.dbe.com.et/", "equity": 37070, "profit": 5738, "price": 1000, "symbol": "DBEETAA", "industry": "Development Banking", "ownership": "State"},
    {"name": "ZamZam Bank", "website": "https://v2.zamzambank.com/", "equity": None, "profit": 24, "price": 1000, "symbol": "ZAMZETAA"},
    {"name": "Hijra Bank", "website": "https://www.hijra-bank.com/", "equity": 1195, "profit": 28, "price": 1000, "symbol": "HIJRETAA"},
    {"name": "Siinqee Bank", "website": "https://www.siinqeebank.com/", "equity": 8479, "profit": 285, "price": 1000, "symbol": "SINQETAA"},
    {"name": "Shabelle Bank", "website": "http://www.shabellebank.com/", "equity": 669, "profit": 20, "price": 1000, "symbol": "SBEEETAA"},
    {"name": "Ahadu Bank", "website": "https://www.ahadubank.com/", "equity": 3096, "profit": -194, "price": 1000, "symbol": "AHUUETAA"},
    {"name": "Goh Betoch Bank SC", "website": "https://www.gohbetbank.com/", "equity": 1545, "profit": 5, "price": 1000, "symbol": "GOBTETAA"},
    {"name": "Tsedey Bank", "website": "https://tsedeybank-sc.com", "equity": 12320, "profit": 1055, "price": 1000, "symbol": "TSDYETAA"},
    {"name": "Gadaa Bank SC", "website": "https://gadaabank.com.et/", "equity": 808, "profit": -84, "price": 1000, "symbol": "GDAAETAA"},
    {"name": "Rammis Bank", "website": "https://www.rammisbank.et/", "equity": 747, "profit": None, "price": 1000, "symbol": "RMSIETAA"},
    {"name": "Ethio Telecom Share Company", "website": "https://www.ethiotelecom.et/", "equity": None, "profit": None, "price": 300, "symbol": "TELE", "ownership": "State", "regulator": "Ethiopian Communications Authority", "industry": "Telecommunications"}
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

def confidence_level(bank):
    if bank['price'] < 500 or (bank.get('equity') and bank['equity'] > 20000):
        return 'High'
    if bank.get('profit') and bank['profit'] > 500:
        return 'High'
    if bank.get('profit') and bank['profit'] > 0:
        return 'Medium'
    return 'Low'

def build_scores(bank):
    pe, eps = implied_pe(bank.get('equity'), bank.get('profit'), bank['price'])
    target = (eps / 0.2) if eps else None
    financial_health = 2 if bank.get('profit') and bank['profit'] > 0 else 1 if bank.get('profit') == 0 else 0
    business_strength = 2 if bank.get('profit') and bank['profit'] >= 500 else 1
    return {
        'pe': pe,
        'eps': eps,
        'current_price': bank['price'],
        'target_price_for_20pc': target,
        'economy_score': 2,
        'industry_score': 2,
        'business_strength_score': business_strength,
        'financial_health_score': financial_health,
        'valuation_score': valuation_score(pe),
        'valuation_notes': f"Assumed price {bank['price']} ETB -> implied P/E {pe or 'N/A'}.",
        'confidence': confidence_level(bank),
    }

def asset_payload(bank):
    price = bank['price']
    name = f"{bank['symbol']} equity" if bank.get('symbol') else f"{bank['name']} Equity"
    return {
        'name': name,
        'asset_type': 'Listed Equity' if bank['price'] < 500 else 'Private Share',
        'market': 'ESX' if bank['price'] < 500 else 'ESX / OTC',
        'transaction_costs': 'Brokerage fee + ESX clearing; assumed ESX-style commissions.',
        'purchase_procedure': f"Open ESX investor account, complete KYC, fund with ETB, and buy at approx {price} per share.",
        'eligibility_requirements': 'ESX-licensed intermediary access and local KYC.',
        'currency': 'ETB',
        'status': 'Tracked'
    }

def source_payload(bank):
    return [
        {
            'source_type': 'Wikipedia list',
            'title': f"{bank['name']} entry on List of banks in Ethiopia",
            'url': 'https://en.wikipedia.org/wiki/List_of_banks_in_Ethiopia',
            'source_date': '2026-03-10',
            'excerpt': 'Equity, profit, and founding info pulled from the Wikipedia table.',
            'reliability': 'Medium'
        },
        {
            'source_type': 'Corporate website',
            'title': f"{bank['name']} official website",
            'url': bank['website'],
            'source_date': '2026-03-10',
            'excerpt': 'Used to verify regulator, service offering, and contact details.',
            'reliability': 'High'
        }
    ]

app = create_app()
with app.app_context():
    db = get_db()
    for bank in banks_data:
        db.execute('DELETE FROM assets WHERE company_id IN (SELECT id FROM companies WHERE name = ?)', (bank['name'],))
        db.execute('DELETE FROM sources WHERE company_id IN (SELECT id FROM companies WHERE name = ?)', (bank['name'],))
        db.execute('DELETE FROM scores WHERE company_id IN (SELECT id FROM companies WHERE name = ?)', (bank['name'],))
        db.execute('DELETE FROM companies WHERE name = ?', (bank['name'],))
    db.commit()

    for bank in banks_data:
        scores = build_scores(bank)
        contact = corporate_contacts.get(bank['name'], {})
        payload = {
            'name': bank['name'],
            'sector': 'Financial Services' if bank.get('industry', 'Banking & Financial Services') == 'Banking & Financial Services' else bank['industry'],
            'industry': bank.get('industry', 'Banking & Financial Services'),
            'ownership_type': bank.get('ownership', 'Private'),
            'regulator': bank.get('regulator', 'National Bank of Ethiopia'),
            'website': bank['website'],
            'status': 'Tracked',
            'industry_analysis': f"{bank['name']} plays in Ethiopia's reforming banking sector; growth is tied to digitization and deposit mobilization.",
            'financial_analysis': f"Equity {bank.get('equity')}m ETB vs profit {bank.get('profit')}m ETB (implied EPS {scores['eps']}).",
            'economy_notes': 'Macroeconomic tailwinds include population growth plus diaspora remittances.',
            'industry_notes': 'Banking is regulated by the NBE with high capital requirements and limited competition.',
            'business_notes': 'Market strength depends on deposit franchise, branch count, and upcoming ESX readiness.',
            'financial_notes': 'Financials derived from published equity/profit data in March 2026.',
            'valuation_notes': scores['valuation_notes'],
            'confidence': scores['confidence'],
            'eps': scores['eps'],
            'implied_pe': scores['pe'],
            'current_price': scores['current_price'],
            'target_price_for_20pc': scores['target_price_for_20pc'],
            'contact_phone': contact.get('contact_phone', ''),
            'contact_email': contact.get('contact_email', ''),
            'contact_address': contact.get('contact_address', ''),
            'investor_notes': contact.get('investor_notes', 'Use the bank website and your ESX intermediary as the next step.'),
            **{k: scores[k] for k in ['economy_score', 'industry_score', 'business_strength_score', 'financial_health_score', 'valuation_score']}
        }
        company_id = create_company(payload)
        create_asset(company_id, asset_payload(bank))
        for source in source_payload(bank):
            add_source(company_id, source)

print('Bank dataset loaded into SQLite.')
