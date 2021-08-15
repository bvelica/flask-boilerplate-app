
from flask import Flask

### Importing the blueprints
from .blueprints.site.routes import blueprint_site
from .blueprints.users.routes import blueprint_users
### End import blueprint

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    ### Register the blueprints
    app.register_blueprint(blueprint_site)
    app.register_blueprint(blueprint_users)
    ### End register blueprints

    return app
