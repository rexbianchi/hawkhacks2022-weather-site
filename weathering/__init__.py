from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = "gksfjskfjskjfak"

    from . import views
    app.register_blueprint(views.bp)
    app.add_url_rule("/", endpoint="search")

    return app
