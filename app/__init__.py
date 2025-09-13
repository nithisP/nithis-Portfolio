from flask import Flask


def create_app():
    app = Flask(__name__)

    # Configuration placeholder
    app.config.from_mapping(
        SECRET_KEY='dev',  # change in production
    )

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
