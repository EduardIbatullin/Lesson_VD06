from flask import Flask
from flask_wtf import CSRFProtect

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

    csrf.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
