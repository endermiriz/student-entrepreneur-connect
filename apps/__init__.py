from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
mail = Mail()


def register_extensions(app):
    mail.init_app(app)

def create_app(config):
    app.config.from_object(config)
    register_extensions(app)
    return app