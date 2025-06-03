import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    # Get the title from the request's parameters
    title = request.args.get("title")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    # Connect to the database
    conn = get_db_connection()

    # Execute a SQL query to select the post with the specified title
    cursor = conn.execute(f"""SELECT * FROM posts WHERE title = '{title}'""")

    if not cursor.fetchone():
        return jsonify({"error": "Post not found"}), 404

    # Fetch the post's content and return it as JSON
    post_content = {
        "id": cursor.lastrowid,
        "title": title,
        "body": cursor.description[1][0].value,
    }

    return jsonify(post_content)
