from app.views.web.factory import create_app
from app.views.web.config import DevelopmentConfig

app = create_app(config=DevelopmentConfig)


def main():
    app.run()


if __name__ == "__main__":
    main()
