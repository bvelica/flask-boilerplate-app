
from flask import Flask

### Importing the blueprints
from .main_site.routes import main_site
from .main_users.routes import main_users


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    ### Register the blueprint
    app.register_blueprint(main_site)
    app.register_blueprint(main_users)

    return app
