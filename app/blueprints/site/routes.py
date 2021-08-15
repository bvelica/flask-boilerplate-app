
from flask import Blueprint

blueprint_site = Blueprint('site', __name__)

@site.route('/')
def index():
	return 'My first index page with blueprint - main page'
