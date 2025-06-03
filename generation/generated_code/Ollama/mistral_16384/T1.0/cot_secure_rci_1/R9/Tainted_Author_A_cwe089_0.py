from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_account():
    conn = get_db_connection()
    title = request.args.get("title")
    cursor = conn.execute("SELECT content FROM Posts WHERE title=?", (title,))
    post = cursor.fetchone()
    if post:
        return jsonify({"content": post["content"]})
    else:
        return "Post not found.", 404


@app.route("/get_post")
def get_account():
    pass  # Leave this line as it is, we will overwrite the method below


# Implement the get_account() function here
