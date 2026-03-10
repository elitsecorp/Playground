INSERT INTO companies (
    name, sector, industry, ownership_type, regulator, website, status,
    industry_analysis, financial_analysis
) VALUES
(
    'Commercial Bank of Ethiopia',
    'Financial Services',
    'Banking',
    'State-Owned',
    'National Bank of Ethiopia',
    'https://www.combanketh.et',
    'Tracked',
    'Banking demand remains strong because salary accounts, trade finance, and payments activity are deeply tied to the formal economy. The industry is competitive, but scale and branch density remain strong structural advantages.',
    'The bank likely benefits from deposit scale and recurring fee income, but detailed valuation and peer-comparable metrics still require current audited statements.'
),
(
    'Ethio Telecom',
    'Communication Services',
    'Telecommunications',
    'State-Owned',
    'Ethiopian Communications Authority',
    'https://www.ethiotelecom.et',
    'Tracked',
    'Telecom remains a strategic infrastructure sector with high barriers to entry, recurring demand, and room for digital service expansion.',
    'Financial performance is often supported by network scale and payment ecosystem growth, though valuation work depends on fuller public disclosures.'
),
(
    'Dashen Bank',
    'Financial Services',
    'Banking',
    'Private',
    'National Bank of Ethiopia',
    'https://www.dashenbanksc.com',
    'Tracked',
    'Private banking remains attractive where strong funding bases, digital channels, and corporate relationships create durable competitive positions.',
    'The key financial questions are loan quality, deposit cost, capital strength, and earnings consistency across inflation cycles.'
);

INSERT INTO scores (
    company_id, economy_score, industry_score, business_strength_score,
    financial_health_score, valuation_score, total_score, rating,
    economy_notes, industry_notes, business_notes, financial_notes,
    valuation_notes, confidence
) VALUES
(
    1, 2, 2, 2, 1, 1, 8, 'Good',
    'Government-linked banking activity and national scale support resilience.',
    'Banking remains essential, regulated, and difficult to enter at scale.',
    'Large branch network, trust, and public-sector relationships are major strengths.',
    'Likely strong deposit base, though current audited ratios need to be refreshed.',
    'Valuation is still provisional because tradable market pricing is limited.',
    'Medium'
),
(
    2, 2, 2, 2, 1, 0, 7, 'Good',
    'Telecom demand benefits from population growth and digitalization.',
    'Very high barriers to entry support industry attractiveness.',
    'National infrastructure and brand trust create strong competitive positioning.',
    'Cash generation may be strong, but public financial depth is still limited.',
    'No robust public market price available in this draft dataset.',
    'Medium'
),
(
    3, 2, 1, 1, 1, 1, 6, 'Moderate',
    'Private banking should benefit from continued formalization and payments growth.',
    'Industry is attractive but crowded among leading banks.',
    'Brand and distribution are solid, though dominance is not absolute.',
    'Financial strength requires current statement verification.',
    'Valuation depends on transaction evidence and updated book value.',
    'Medium'
);

INSERT INTO assets (
    company_id, name, asset_type, market, transaction_costs,
    purchase_procedure, eligibility_requirements, currency, status
) VALUES
(
    1,
    'Commercial Bank of Ethiopia Equity Interest',
    'Private Share / Restricted Equity',
    'Off-market',
    'Transaction costs depend on transfer fees, legal documentation, and any intermediary costs.',
    'Confirm transfer eligibility, verify seller documentation, obtain regulator or issuer approvals where required, and complete transfer through the recognized process.',
    'Buyer must confirm legal eligibility and document verification requirements.',
    'ETB',
    'Research'
),
(
    2,
    'Telebirr Ecosystem Exposure',
    'Strategic Operating Asset',
    'Not directly tradable',
    'Not applicable for direct public purchase in this draft.',
    'Exposure is indirect unless a future public instrument becomes available.',
    'Not currently structured as a general public market purchase instrument.',
    'ETB',
    'Research'
),
(
    3,
    'Dashen Bank Share Transfer',
    'Private Share',
    'Off-market',
    'Seller and buyer should verify transfer fees, notarization, taxes, and brokerage costs if any.',
    'Identify seller, verify share certificate or register evidence, confirm issuer transfer rules, then submit the transfer package for approval and registration.',
    'Buyer identity, KYC, and issuer approval requirements may apply.',
    'ETB',
    'Research'
);

INSERT INTO sources (
    company_id, source_type, title, url, source_date, excerpt, reliability
) VALUES
(
    1,
    'Official Website',
    'Commercial Bank of Ethiopia official website',
    'https://www.combanketh.et',
    '2026-03-10',
    'Used as a primary reference for company identity and public positioning.',
    'High'
),
(
    2,
    'Official Website',
    'Ethio Telecom official website',
    'https://www.ethiotelecom.et',
    '2026-03-10',
    'Used as a primary reference for company identity and telecom service footprint.',
    'High'
),
(
    3,
    'Official Website',
    'Dashen Bank official website',
    'https://www.dashenbanksc.com',
    '2026-03-10',
    'Used as a primary reference for company identity and banking products.',
    'High'
);
