import sqlite3
from flask import Flask, request
import json

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
    title = request.args.get('title', '')
    if not title:
        return 'Title parameter is required', 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM posts WHERE title = ?', (title,))
    post = cursor.fetchone()

    if not post:
        conn.close()
        return json.dumps({'error': 'Post not found'}), 404

    content = str(post['content'])
    conn.close()
    return json.dumps({'content': content})