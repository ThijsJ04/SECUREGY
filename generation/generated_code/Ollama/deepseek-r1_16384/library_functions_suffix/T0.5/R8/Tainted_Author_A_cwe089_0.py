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
        return jsonify({'error': 'Title is required'}), 400

    db_conn = get_db_connection()
    cursor = db_conn.cursor()

    query = "SELECT content FROM posts WHERE title = ?"
    cursor.execute(query, (title,))

    row = cursor.fetchone()

    if not row:
        return jsonify({'error': 'Post not found'}), 404

    post_content = row['content']
    db_conn.close()

    return jsonify({'content': post_content}), 200