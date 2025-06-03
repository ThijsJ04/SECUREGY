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
        return "Title parameter is required"

    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT content FROM posts WHERE title = ?;"
    cursor.execute(query, (title,))
    result = cursor.fetchall()

    if len(result) == 0:
        conn.close()
        return "Post not found"
    else:
        content = result[0]["content"]
        conn.close()
        return content
