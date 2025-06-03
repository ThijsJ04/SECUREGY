import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title", "").strip()
    if not title:
        return "Title parameter is required"

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT content FROM posts 
                WHERE title LIKE ? COLLATE NOCASE
            """,
                (title,),
            )

            post = cursor.fetchone()
            if post:
                return post["content"]
            else:
                return "Post not found"
    except sqlite3.Error as e:
        return f"Error fetching post: {str(e)}"
