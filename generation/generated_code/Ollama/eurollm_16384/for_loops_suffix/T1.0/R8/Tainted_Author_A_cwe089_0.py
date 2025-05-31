import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')
    try:
        with get_db_connection() as conn:
            cur = conn.cursor()
            query = "SELECT * FROM posts WHERE title=?"
            cur.execute(query, (title,))
            post = cur.fetchone()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 404

    data = {}
    data['post_id'] = post[0] if post else None
    data['title'] = post[1] if post else None
    data['content'] = post[2] if post else None
    return jsonify(data)