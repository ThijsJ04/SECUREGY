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
        return jsonify({"error": "Title is required"}), 400

    try:
        db = get_db_connection()
        cursor = db.execute("SELECT * FROM posts WHERE title = ?", (title,))
        post = cursor.fetchone()

        if not post:
            return jsonify({"error": f"Post with title {title} not found"}), 404

        return jsonify({"content": post["content"]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()
