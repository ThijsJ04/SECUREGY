import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title', None)
    if not title:
        return jsonify({'error': 'Title parameter is required'}), 400
    conn = get_db_connection()
    try:
        cursor = conn.execute("SELECT content FROM posts WHERE title = ?", (title,))
        post_row = cursor.fetchone()
        if post_row:
            return jsonify({'content': post_row['content']})
        else:
            return jsonify({'error': 'Post not found'}), 404
    finally:
        conn.close()