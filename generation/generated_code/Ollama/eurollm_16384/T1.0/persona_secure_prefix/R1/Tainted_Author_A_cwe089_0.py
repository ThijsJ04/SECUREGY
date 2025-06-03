from flask import Flask, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    # Get the title from the request parameters
    title = request.args.get("title")

    if not title:
        return "Error: Title is required", 400

    conn = get_db_connection()
    query = """SELECT * FROM posts WHERE title = ?"""
    cur = conn.cursor()
    cur.execute(query, (title,))
    result = cur.fetchone()
    conn.close()

    if result is None:
        return "Post not found", 404

    post_data = {"id": result[0], "content": result[1]}

    return str(post_data)
