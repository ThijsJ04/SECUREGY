import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    if not title:
        return "No title provided"

    with get_db_connection() as conn:
        cursor = conn.execute('SELECT * FROM posts WHERE title = ?', (title,))
        posts = cursor.fetchall()

        if not posts:
            return f"No post found with title: {title}"

        content_list = [post['content'] for post in posts]
        return ', '.join(content_list)