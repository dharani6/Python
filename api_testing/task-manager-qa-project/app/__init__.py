from flask import Flask


def create_app():
    """Application factory so tests can spin up isolated app instances."""
    app = Flask(__name__)
    from .routes import bp
    app.register_blueprint(bp)
    return app
