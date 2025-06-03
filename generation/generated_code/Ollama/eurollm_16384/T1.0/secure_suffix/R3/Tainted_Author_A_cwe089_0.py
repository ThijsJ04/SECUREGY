import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title", default="", type=str)
    if not title:
        return "Error: Missing required parameter 'title'", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    post_query = """SELECT content FROM posts WHERE title = ?"""
    record = cursor.execute(post_query, (title,))
    content = record.fetchone()
    conn.close()

    if not content:
        return "No post found with the given title", 404

    return str(content[0]) + "\n"
