import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    conn = get_db_connection()
    query = "SELECT title, content FROM posts WHERE title = ?"
    result = conn.execute(query, (request.args.get("title"),))
    post = result.fetchone()
    conn.close()
    return {"post": post} if post else None
