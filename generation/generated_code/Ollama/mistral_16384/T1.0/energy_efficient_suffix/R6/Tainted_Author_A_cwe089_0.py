from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title")  # Get the title from the request's parameters.
    if not title:
        return jsonify({"error": "Title is required."}), 400

    conn = get_db_connection()  # Get a database connection.
    cursor = conn.cursor()  # Prepare a cursor object.

    cursor.execute(
        "SELECT content FROM posts WHERE title=?", (title,)
    )  # Execute the query to fetch the post's content.
    post = cursor.fetchone()  # Fetch the result of the executed query.

    if not post:
        return jsonify({"error": "Post with that title does not exist."}), 404

    conn.close()  # Close the database connection after use.

    return jsonify(post._asdict())  # Return the post's content in JSON format.
