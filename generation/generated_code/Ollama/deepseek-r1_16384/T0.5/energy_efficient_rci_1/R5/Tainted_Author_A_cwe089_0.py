import sqlite3

from flask import Flask, request

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
    try:
        title = request.args.get("title", default="", type=str)
        if not title:
            return {"error": "Title parameter is required"}, 400

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT content FROM posts WHERE title = ?"
        cursor.execute(query, (title,))

        result = cursor.fetchall()
        if len(result) == 0:
            return {"message": "Post not found"}, 404

        post_content = dict(result[0])
        conn.close()
        return post_content

    except sqlite3.Error as e:
        return {"error": str(e)}, 500
    finally:
        if "conn" in locals():
            conn.close()
