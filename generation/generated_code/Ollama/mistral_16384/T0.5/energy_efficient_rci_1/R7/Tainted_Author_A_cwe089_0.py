from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title", None)
    if not title:
        return jsonify({"error": 'Missing required parameter "title".'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    post = cursor.fetchone()

    if not post:
        return jsonify({"error": "Post with the given title does not exist."}), 404

    conn.close()
    return jsonify({"content": post["content"]})
