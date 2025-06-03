import secrets
from flask import request, jsonify
from sqlalchemy import desc

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

    if not username or not token:
        return jsonify({"message": "Missing required parameters"})

    query = User.query \
           .filter(User.username == username) \
           .order_by(desc(User.id)) \  # Sort by ID for primary key check
           .first()

    if query:
        if hash_password(token).compare(query.token):
            return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})