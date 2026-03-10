def total_score(row):
    return (
        row["economy_score"]
        + row["industry_score"]
        + row["business_strength_score"]
        + row["financial_health_score"]
        + row["valuation_score"]
    )


def rating_for(score):
    if score >= 9:
        return "Strong"
    if score >= 7:
        return "Good"
    if score >= 5:
        return "Moderate"
    return "Avoid"


def normalize_scores(payload):
    fields = [
        "economy_score",
        "industry_score",
        "business_strength_score",
        "financial_health_score",
        "valuation_score",
    ]
    normalized = {}
    for field in fields:
        value = int(payload.get(field, 0))
        normalized[field] = max(0, min(2, value))
    total = total_score(normalized)
    normalized["total_score"] = total
    normalized["rating"] = rating_for(total)
    return normalized
