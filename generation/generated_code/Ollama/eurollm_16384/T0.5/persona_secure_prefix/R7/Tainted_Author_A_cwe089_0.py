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
    if not title:
        return "Error: Title is required", 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
        result = cursor.fetchone()
        if result is None:
            return "Post not found", 404
        else:
            post_content = result[0]
            conn.close()
            return post_content
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return f"Error: {e}"
