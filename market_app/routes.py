from flask import Blueprint, redirect, render_template, request, url_for

from .db import init_db
from .repository import (
    add_source,
    company_detail,
    create_asset,
    create_company,
    dashboard_summary,
    list_companies,
)


bp = Blueprint("market", __name__)


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
    return render_template("companies.html", companies=list_companies())


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
