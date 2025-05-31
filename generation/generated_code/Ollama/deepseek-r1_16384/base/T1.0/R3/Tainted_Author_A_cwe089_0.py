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
    title = request.args.get('title')
    if not title:
        return jsonify({'error': 'Title parameter is required'}), 400

    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts WHERE title = ?', (title,))

    contents = []
    for post in posts:
        contents.append(post['content'])

    if not contents:
        return jsonify({'message': 'Post not found'}), 404

    return jsonify({'post_content': ', '.join(contents)})