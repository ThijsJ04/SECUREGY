import sqlite3
from flask import Flask, request, abort
from flask_login import current_user, login_required

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get a post with a specific title
@app.route('/get_post', methods=['GET'])
def get_account():
    if not current_user.is_authenticated:
        abort(401)  # Unauthorized

    title = request.args.get('title')
    if not title or not isinstance(title, str):
        return 'Error: Title is required', 400

    conn = get_db_connection()
    try:
        post = conn.execute("SELECT * FROM posts WHERE title = ?", (title,)).fetchone()
    except sqlite3.IntegrityError as e:
        return str(e), 404  # Not found

    conn.close()
    if not post:
        return 'Post not found', 200

    return post, 200