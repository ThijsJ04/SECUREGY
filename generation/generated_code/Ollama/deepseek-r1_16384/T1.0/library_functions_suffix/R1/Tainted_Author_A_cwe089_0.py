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

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))
    result = cursor.fetchone()

    if result:
        return jsonify({"content": result["content"]}), 200
    else:
        return jsonify({"error": "Post not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
