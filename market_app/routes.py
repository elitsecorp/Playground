from flask import Blueprint, redirect, render_template, request, url_for

from .db import init_db
from .repository import (
    add_source,
    company_detail,
    create_asset,
    create_company,
    dashboard_summary,
    list_industries,
    query_companies,
)


bp = Blueprint("market", __name__)


def parse_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


@bp.route("/")
def index():
    summary, top_companies = dashboard_summary()
    return render_template("index.html", summary=summary, top_companies=top_companies)


@bp.route("/setup")
def setup():
    init_db()
    return redirect(url_for("market.index"))


@bp.route("/companies")
def companies():
    raw_min_score = request.args.get("min_score", "").strip()
    numeric_min_score = parse_int(raw_min_score)
    query_filters = {
        "industry": request.args.get("industry", "").strip(),
        "search": request.args.get("search", "").strip(),
        "sort": request.args.get("sort", "score"),
    }
    if numeric_min_score is not None:
        query_filters["min_score"] = numeric_min_score

    companies = query_companies(query_filters)
    industries = list_industries()
    return render_template(
        "companies.html",
        companies=companies,
        industries=industries,
        filters={
            "industry": query_filters["industry"],
            "min_score": raw_min_score,
            "search": query_filters["search"],
            "sort": query_filters["sort"],
        },
    )


@bp.route("/companies/new", methods=["GET", "POST"])
def company_new():
    if request.method == "POST":
        company_id = create_company(request.form)
        return redirect(url_for("market.company_view", company_id=company_id))
    return render_template("company_form.html")


@bp.route("/companies/<int:company_id>")
def company_view(company_id):
    company, assets, sources = company_detail(company_id)
    return render_template(
        "company_detail.html",
        company=company,
        assets=assets,
        sources=sources,
    )


@bp.route("/companies/<int:company_id>/assets/new", methods=["POST"])
def asset_new(company_id):
    create_asset(company_id, request.form)
    return redirect(url_for("market.company_view", company_id=company_id))


@bp.route("/companies/<int:company_id>/sources/new", methods=["POST"])
def source_new(company_id):
    add_source(company_id, request.form)
    return redirect(url_for("market.company_view", company_id=company_id))
