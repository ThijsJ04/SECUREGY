import sqlite3
import json

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
    # Get title parameter from request
    title = request.args.get("title")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    # Connect to database and fetch post by title
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE title = ?", (title,)).fetchone()

    if not post:
        return jsonify({"error": "No post found with this title"}), 404

    # Return content of the post in JSON format
    return jsonify({"content": str(post["content"])})
