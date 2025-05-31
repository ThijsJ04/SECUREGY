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
    title = request.args.get('title')

    if not title:
        return 'Missing title parameter', 400

    db_conn = get_db_connection()
    cursor = db_conn.cursor()

    cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))
    result = cursor.fetchone()

    db_conn.close()

    if not result:
        return f'Post with title: {title} does not exist', 404

    return result['content']