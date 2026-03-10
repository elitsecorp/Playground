DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS assets;
DROP TABLE IF EXISTS scores;
DROP TABLE IF EXISTS sources;

CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    sector TEXT NOT NULL DEFAULT '',
    industry TEXT NOT NULL DEFAULT '',
    ownership_type TEXT NOT NULL DEFAULT '',
    regulator TEXT NOT NULL DEFAULT '',
    website TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'Research',
    industry_analysis TEXT NOT NULL DEFAULT '',
    financial_analysis TEXT NOT NULL DEFAULT '',
    contact_phone TEXT NOT NULL DEFAULT '',
    contact_email TEXT NOT NULL DEFAULT '',
    contact_address TEXT NOT NULL DEFAULT '',
    investor_notes TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL UNIQUE,
    economy_score INTEGER NOT NULL DEFAULT 0,
    industry_score INTEGER NOT NULL DEFAULT 0,
    business_strength_score INTEGER NOT NULL DEFAULT 0,
    financial_health_score INTEGER NOT NULL DEFAULT 0,
    valuation_score INTEGER NOT NULL DEFAULT 0,
    total_score INTEGER NOT NULL DEFAULT 0,
    rating TEXT NOT NULL DEFAULT 'Avoid',
    economy_notes TEXT NOT NULL DEFAULT '',
    industry_notes TEXT NOT NULL DEFAULT '',
    business_notes TEXT NOT NULL DEFAULT '',
    financial_notes TEXT NOT NULL DEFAULT '',
    valuation_notes TEXT NOT NULL DEFAULT '',
    confidence TEXT NOT NULL DEFAULT 'Low',
    eps REAL NOT NULL DEFAULT 0,
    implied_pe REAL NOT NULL DEFAULT 0,
    current_price REAL NOT NULL DEFAULT 0,
    target_price_for_20pc REAL NOT NULL DEFAULT 0,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies (id)
);

CREATE TABLE assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    asset_type TEXT NOT NULL DEFAULT '',
    market TEXT NOT NULL DEFAULT '',
    transaction_costs TEXT NOT NULL DEFAULT '',
    purchase_procedure TEXT NOT NULL DEFAULT '',
    eligibility_requirements TEXT NOT NULL DEFAULT '',
    currency TEXT NOT NULL DEFAULT 'ETB',
    status TEXT NOT NULL DEFAULT 'Research',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies (id)
);

CREATE TABLE sources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    source_type TEXT NOT NULL DEFAULT 'Website',
    title TEXT NOT NULL,
    url TEXT NOT NULL DEFAULT '',
    source_date TEXT,
    excerpt TEXT NOT NULL DEFAULT '',
    reliability TEXT NOT NULL DEFAULT 'Medium',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies (id)
);
