import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get("title", "")
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT content FROM posts WHERE title = ?", (title,))
        post = cur.fetchone()
        if post:
            return jsonify({"content": str(post["content"])})
        else:
            return jsonify({"content": ""})
    finally:
        conn.close()
