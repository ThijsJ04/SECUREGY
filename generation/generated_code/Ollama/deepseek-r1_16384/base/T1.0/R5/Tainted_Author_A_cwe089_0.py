import sqlite3

from flask import Flask, request

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
    if 'title' not in request.args:
        return "Error: No title provided"

    title = request.args['title']

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT content FROM posts WHERE title = ?', (title,))
        row = cursor.fetchone()

        if row is None:
            return "Post not found"
        else:
            return str(row['content'])