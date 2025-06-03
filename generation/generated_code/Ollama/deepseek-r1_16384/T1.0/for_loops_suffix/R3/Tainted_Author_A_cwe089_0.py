import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_db_context():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


@app.route("/get_post")
def get_account():
    title = request.args.get("title")

    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    with get_db_context() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))
        result = cursor.fetchone()

        if result:
            return jsonify({"content": result["content"]})
        else:
            return jsonify({"error": f"Post with title {title} not found"}), 404
