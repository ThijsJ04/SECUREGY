import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title")
    conn = get_db_connection()
    posts = conn.execute("SELECT content FROM posts WHERE title = ?", (title,))
    result = posts.fetchone()
    if result:
        return str(result["content"])
    else:
        return "Post not found"


if __name__ == "__main__":
    app.run(debug=True)
