from flask import Flask

from .db import close_db, init_app
from .routes import bp


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=app.instance_path + "/market_intelligence.sqlite3",
        SECRET_KEY="dev",
    )

    init_app(app)
    app.register_blueprint(bp)

    app.teardown_appcontext(close_db)

    return app
