import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    title = request.args.get("title")
    conn = get_db_connection()
    query = "SELECT * FROM posts WHERE title = ?"
    rows = conn.execute(query, (title,))
    if not rows:  # Check if any post with the given title exists
        return "No posts found with that title", 404
    post_data = rows[0]  # Assuming only one row is returned
    conn.close()
    return str(post_data)
