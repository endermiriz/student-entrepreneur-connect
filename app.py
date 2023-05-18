from apps import create_app
from apps.config import Config

app = create_app(Config)


if __name__ == "__main__":
    app.run(debug=True)
