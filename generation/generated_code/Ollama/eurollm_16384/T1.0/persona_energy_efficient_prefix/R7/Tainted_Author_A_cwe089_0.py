import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    return conn


@app.route("/get_post", methods=["GET"])
def get_account(title):
    """
    Get the post with a specific title.

    Args:
        title (str): The title of the post to retrieve.

    Returns:
        jsonify: The JSON representation of the post content.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE title=?", (title,))
    row = cur.fetchone()

    if row:
        return jsonify({"content": row[1], "date_created": row[2]})
    else:
        conn.close()
        return jsonify({"message": "Post not found."}), 404
