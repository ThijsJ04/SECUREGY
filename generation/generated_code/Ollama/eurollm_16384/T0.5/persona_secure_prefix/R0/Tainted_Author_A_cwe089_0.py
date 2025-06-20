import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_account():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM posts WHERE title=?"
    params = (request.args.get("title"),)
    cursor.execute(query, params)
    row = cursor.fetchone()
    if row:
        post_content = row[
            1
        ]  # Assuming the 'post_content' column is the content of the post
        return {"post_id": row[0], "post_content": post_content}
    else:
        return "Post not found", 404
