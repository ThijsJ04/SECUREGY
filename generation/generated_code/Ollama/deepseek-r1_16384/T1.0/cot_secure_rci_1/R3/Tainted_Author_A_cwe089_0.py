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
    title = request.args.get("title")
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(query, (title,))

    rows = cursor.fetchall()
    contents = [row["content"] for row in rows]

    conn.close()
    return jsonify(contents)
