import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    if not title:
        return "Title parameter is required", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE title = ?", (title,))
    post = cursor.fetchone()

    conn.close()

    if not post:
        return "Post not found", 404
    return jsonify({'content': post['content']})