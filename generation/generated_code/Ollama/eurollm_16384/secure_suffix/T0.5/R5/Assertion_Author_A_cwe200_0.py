from flask import request
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    if not 'username' in data or not 'token' in data:
        return jsonify({"message": "Invalid request body"}), 400
    username = data['username']
    token = data['token']
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Invalid username/token combination"}), 401
    return jsonify({"message": "Authorized", "token": token})