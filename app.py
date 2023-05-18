from apps import create_app
from apps.config import Config

app = create_app(Config)


if __name__ == "__main__":
    # Debug mode can be controlled in .env with
    # FLASK_DEBUG variable.
    app.run()
