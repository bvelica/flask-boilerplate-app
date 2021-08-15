
from flask import Blueprint

blueprint_users = Blueprint('users', __name__, url_prefix='/users')

@main_users.route('/')
def users():
	return 'Users page - blueprint users'
