from flask import Blueprint, request, session
from flask_bcrypt import Bcrypt
from models.user_model import UserModel
from views.auth_views import AuthViews

bcrypt = Bcrypt()
auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return AuthViews.signup_failure('Username and password are required')

    if UserModel.find_by_username(username):
        return AuthViews.signup_failure('User already exists')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    result = UserModel.create_user(username, hashed_password)

    return AuthViews.signup_success(str(result.inserted_id))

@auth_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return AuthViews.login_failure()

    user = UserModel.find_by_username(username)
    if user and bcrypt.check_password_hash(user['password'], password):
        session['user_id'] = str(user['_id'])
        return AuthViews.login_success(UserModel.serialize(user))
    else:
        return AuthViews.login_failure()

@auth_controller.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return AuthViews.logout_success()

@auth_controller.route('/status', methods=['GET'])
def status():
    if 'user_id' in session:
        user = UserModel.find_by_id(session['user_id'])
        if user:
            return AuthViews.login_status(True, UserModel.serialize(user))
    return AuthViews.login_status(False)
