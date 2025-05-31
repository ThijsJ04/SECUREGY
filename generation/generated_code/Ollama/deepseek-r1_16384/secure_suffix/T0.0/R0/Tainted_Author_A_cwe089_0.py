import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)
    if not title:
        return jsonify({'error': 'Title is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT content FROM posts WHERE title = %s"
    cursor.execute(query, (title,))

    rows = cursor.fetchall()
    if not rows:
        return jsonify({}), 404

    contents = [row['content'] for row in rows]
    cursor.close()
    conn.close()

    return jsonify({'contents': contents})