import os

class Config(object):

    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY', "123456789")
    
    # Flask-Mailman
    MAIL_SERVER = os.getenv('MAIL_SERVER', "smtp.gmail.com")
    MAIL_PORT = os.getenv('MAIL_PORT', 465)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', False)
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', True)
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    MAIL_TIMEOUT = 120
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')