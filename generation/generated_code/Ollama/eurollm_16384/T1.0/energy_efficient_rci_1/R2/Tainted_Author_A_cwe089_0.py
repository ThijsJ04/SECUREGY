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

    # Replace the following line with your actual database connection and query code.
    with get_db_connection() as conn:
        post = conn.execute("SELECT * FROM posts WHERE title=?", (title,)).fetchone()
        if not post:  # if no post found, return a 404 status code
            return {"error": "Post not found"}, 404

    data = str(post or {}).replace("'", "")  # replace single quotes with double quotes
    return data, 200
