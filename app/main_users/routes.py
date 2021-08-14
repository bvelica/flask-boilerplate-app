
from flask import Blueprint

main_users = Blueprint('main_users', __name__, url_prefix='/users')

@main_users.route('/')
def users():
	return 'Users page - blueprint users'
