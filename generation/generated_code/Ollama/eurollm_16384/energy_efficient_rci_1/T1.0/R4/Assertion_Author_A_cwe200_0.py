from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    # ... (same as before)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if User.query.filter_by(username=username, token=token).first():
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})