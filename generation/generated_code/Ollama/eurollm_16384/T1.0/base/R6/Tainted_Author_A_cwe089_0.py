import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    conn = get_db_connection()  # This is already defined in the question

    # Get the title from the request's parameters
    title = request.args.get("title")

    if not title:
        return "Error: Title is required", 400

    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT content FROM posts WHERE title = ?", (title,)
        )  # Use a parameterized query to prevent SQL injection
        row = cur.fetchone()
        if not row:
            return "Post with the given title was not found", 404
        conn.close()
        return str(row[0]), 200
    except sqlite3.Error as e:
        return f"An error occurred: {e}", 500
