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
    conn = get_db_connection()
    title = request.args.get('title')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts WHERE title = ?', (title,))

    posts = cursor.fetchall()

    if not posts:
        return jsonify({"error": "Post not found"}), 404

    post_content = posts[0]['content']
    return jsonify({"content": post_content})