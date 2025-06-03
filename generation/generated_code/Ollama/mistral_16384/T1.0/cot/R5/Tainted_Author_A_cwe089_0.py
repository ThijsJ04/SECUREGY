from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_account(title):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT content FROM posts WHERE title=?", (title,))
    post = cur.fetchone()
    if post:
        post = post["content"]
    else:
        post = "Post not found"
    return post


@app.route("/get_post")
def get_account_api():
    title = request.args.get("title")
    result = get_account(title)
    return jsonify({"content": result})
