import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """Get the post with a specific title."""
    # Fetch the post with the given title using SQL query
    title = request.args.get("title")
    query = "SELECT * FROM posts WHERE title = ?"
    cur = conn.cursor()
    cur.execute(query, (title,))
    row = cur.fetchone()

    if row:
        # Return the post's content as JSON
        data = {"id": row[0], "title": row[1], "content": row[2]}
        return jsonify(data)
    else:
        # Return a 404 error if no post found with the given title
        return jsonify({"error": "No post found"}), 404
