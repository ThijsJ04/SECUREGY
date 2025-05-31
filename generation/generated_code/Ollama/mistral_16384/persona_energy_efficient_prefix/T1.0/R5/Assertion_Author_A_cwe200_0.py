from functools import wraps
import re

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        req_token = kwargs.get('headers').get('X-Token')
        user = User.query.filter_by(token=req_token).first()
        if not user:
            return jsonify({"message": "Unauthorized"})
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})

    return jsonify({"message": "User registered successfully", "token": token})

@app.route('/', methods=['GET'])
@login_required
def home():
    return jsonify({"message": "Authorized"})