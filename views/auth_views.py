from flask import jsonify

class AuthViews:
    @staticmethod
    def signup_success(user_id):
        return jsonify({'message': 'User created successfully', 'user_id': user_id}), 201

    @staticmethod
    def signup_failure(message):
        return jsonify({'error': message}), 400

    @staticmethod
    def login_success(user):
        return jsonify({'message': 'Login successful', 'user': user}), 200

    @staticmethod
    def login_failure():
        return jsonify({'error': 'Invalid username or password'}), 401

    @staticmethod
    def logout_success():
        return jsonify({'message': 'Logged out successfully'}), 200

    @staticmethod
    def login_status(logged_in, user=None):
        if logged_in:
            return jsonify({'logged_in': True, 'user': user}), 200
        return jsonify({'logged_in': False}), 200
