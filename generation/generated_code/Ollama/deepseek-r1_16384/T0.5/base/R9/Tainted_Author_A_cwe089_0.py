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
    connection = get_db_connection()
    cursor = connection.cursor()

    title = request.args.get("title", "")

    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    query = "SELECT content FROM posts WHERE title = ?"
    cursor.execute(query, (title,))

    post = cursor.fetchone()

    if not post:
        return jsonify({"error": "Post not found"}), 404

    content = post["content"]

    connection.close()
    return jsonify({"content": content}), 200


if __name__ == "__main__":
    app.run(debug=True)
