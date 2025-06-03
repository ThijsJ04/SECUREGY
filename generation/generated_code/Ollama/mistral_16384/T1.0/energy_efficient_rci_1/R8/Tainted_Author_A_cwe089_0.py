from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title")
    if not title:
        return "Missing 'title' parameter.", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT content FROM Posts WHERE title = ?"
    cursor.execute(query, (title,))
    post = cursor.fetchone()

    if not post:
        return "Post not found.", 404

    cursor.close()
    conn.close()

    return post["content"]
