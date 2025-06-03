import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account(title):
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    query = "SELECT * FROM posts WHERE title=?"
    result = conn.execute(query, (title,))
    post = result.fetchone()
    conn.close()
    return jsonify({"content": post[1]})
