import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get the title from the request's parameters
    title = request.args.get("title")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    query = f"""SELECT * FROM posts WHERE title = '{title}'"""
    cursor.execute(query)
    result = cursor.fetchone()

    if not result:
        return jsonify({"error": "Post not found"}), 404

    post_content = result[
        1
    ]  # Assuming the content is in the second column of the table

    conn.close()
    return jsonify(post_content)
