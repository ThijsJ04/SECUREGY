import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get("title", type=str)
    if not title:
        return jsonify({"message": "Title parameter is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))
    row = cursor.fetchone()

    if row:
        return jsonify({"content": row["content"]})
    else:
        return jsonify({}), 404


if __name__ == "__main__":
    app.run(debug=True)
