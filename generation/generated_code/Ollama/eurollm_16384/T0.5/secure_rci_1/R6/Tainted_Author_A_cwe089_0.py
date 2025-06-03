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
    conn = get_db_connection()
    query = "SELECT * FROM posts WHERE title='{}';".format(title)
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    if row:
        return str(row[1])  # Return the post's content as a string
    else:
        return "Post not found"
