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
        return "Title is required", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(sql, (title,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return "Post with the given title not found", 404

    return str(result)
