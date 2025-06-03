import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title", "")
    if not title:
        return "Title parameter is required", 400

    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    query = "SELECT content FROM posts WHERE title = ?"
    cursor.execute(query, (title,))
    post = cursor.fetchone()

    if post is None:
        return "Post not found", 404
    else:
        return post["content"]


if __name__ == "__main__":
    app.run(debug=True)
