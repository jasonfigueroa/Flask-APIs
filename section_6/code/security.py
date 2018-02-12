from werkzeug.security import safe_str_cmp
from resources.user import User

def authenticate(username, password):
	# the following is alternate syntax for username_mapping[username], where 
	# you can return None if the username is not found
	user = User.find_by_username(username)
	if user and safe_str_cmp(user.password, password):
		return user

def identity(payload):
	user_id = payload['identity']
	return User.find_by_id(user_id)
