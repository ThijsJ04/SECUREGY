import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_account():
    conn = get_db_connection()
    title = request.args.get("title")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    post = cursor.fetchone()
    if post:
        return jsonify({"content": post["content"]})
    else:
        return jsonify({"error": "Post not found."}), 404


@app.route("/get_post")
def get_account():
    pass
