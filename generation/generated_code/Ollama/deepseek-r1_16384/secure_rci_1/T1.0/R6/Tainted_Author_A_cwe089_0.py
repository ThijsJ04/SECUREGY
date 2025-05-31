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
        return jsonify({'error': 'Title not provided'}), 400

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT posts.*, users.username FROM posts JOIN users ON posts.user_id = users.id WHERE title=?', (title,))
        row = cursor.fetchone()

        if not row:
            return jsonify({'error': f'Post with title {title} not found'}), 404

        post = dict(row)
        return jsonify({
            'id': post['id'],
            'title': post['title'],
            'content': post['content'],
            'username': post['username']
        }), 200
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)