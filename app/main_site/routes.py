
from flask import Blueprint

main_site = Blueprint('main_site', __name__)

@main_site.route('/')
def index():
	return 'My first index page with blueprint - main page'
