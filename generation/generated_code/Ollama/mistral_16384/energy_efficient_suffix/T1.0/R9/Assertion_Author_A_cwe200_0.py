from functools import wraps
import time

def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''

    def authenticate(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            data = args[0].get_json()
            username = data.get("username", "")
            token = data.get("token", "")
            user = User.query.filter_by(username=username, token=token).first()
            if user:
                return f(user, *args[1:], **kwargs)
            else:
                return jsonify({"message": "Unauthorized"})
        return decorated

    @authenticate
    def _inner(user, *args, **kwargs):
        db.session.commit()
        return jsonify({"message": "Authorized"})

    return _inner