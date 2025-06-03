import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title")
    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))
        post = cursor.fetchone()

        if post:
            return jsonify({"content": str(post["content"])}), 200
        else:
            return jsonify({"message": "Post not found"}), 404

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if "conn" in locals():
            conn.close()
