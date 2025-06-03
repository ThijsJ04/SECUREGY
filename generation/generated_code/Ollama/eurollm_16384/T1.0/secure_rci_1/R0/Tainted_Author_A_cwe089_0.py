from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    query = "SELECT * FROM posts WHERE title LIKE ? ORDER BY id DESC LIMIT 1;"
    cur = conn.execute(query, ("%",))
    row = cur.fetchone()

    if row:
        return jsonify({"content": row[2], "author": row[3]})
    else:
        return jsonify({"error": "Post not found"}), 404
