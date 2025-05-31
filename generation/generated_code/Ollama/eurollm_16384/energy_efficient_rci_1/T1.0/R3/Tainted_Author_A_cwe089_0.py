from flask import abort, jsonify
from sqlalchemy import desc, func
import sqlite3

app = Flask(__name__)
db = get_db_connection()

@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')
    if not title:
        abort(400, "Please provide a title")

    rows = db.execute("SELECT * FROM posts WHERE title=? ORDER BY id DESC", (title,))
    post_data = rows[0] if len(rows) == 1 else rows[-1]

    return jsonify(post_data), 200