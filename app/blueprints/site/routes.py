
from flask import Blueprint

blueprint_site = Blueprint('site', __name__)

@blueprint_site.route('/')
def index():
	return 'My first index page with blueprint - main page'
