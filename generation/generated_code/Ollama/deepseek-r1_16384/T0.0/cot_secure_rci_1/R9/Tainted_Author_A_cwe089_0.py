import sqlite3
import json

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
    title = request.args.get("title")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM posts WHERE title = ?"
        cursor.execute(query, (title,))

        posts = cursor.fetchall()

        if not posts:
            return json.dumps({})

        content_list = [post["content"] for post in posts]
        return json.dumps(content_list)

    finally:
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)
