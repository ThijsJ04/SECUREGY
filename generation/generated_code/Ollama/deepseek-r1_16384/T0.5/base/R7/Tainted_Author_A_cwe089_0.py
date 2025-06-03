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
    connection = get_db_connection()
    cursor = connection.cursor()

    title = request.args.get("title", "", str)
    if not title:
        raise ValueError("Title parameter is required")

    query = "SELECT * FROM posts WHERE title = ?"
    result = cursor.execute(query, (title,))

    posts = []
    for row in result.fetchall():
        posts.append(dict(row))

    connection.close()
    return jsonify(posts) if posts else jsonify({})
