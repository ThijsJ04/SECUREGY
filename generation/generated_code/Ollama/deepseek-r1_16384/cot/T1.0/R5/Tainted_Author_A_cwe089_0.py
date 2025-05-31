import sqlite3
from flask import Flask, request, abort

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    if not title:
        abort(400)
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT content FROM posts WHERE title = ?", (title,))
        post = cur.fetchone()
        if post is None:
            abort(404)
        return post['content']
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        abort(500)
    finally:
        conn.close()