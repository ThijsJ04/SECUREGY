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
    title = request.args.get('title')
    if not title:
        return "Title parameter is required"

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT content FROM posts WHERE title = ? LIMIT 1", (title,))
        post = cursor.fetchone()
        if post:
            return json.dumps({'content': post['content']})
        else:
            return "Post not found"
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)