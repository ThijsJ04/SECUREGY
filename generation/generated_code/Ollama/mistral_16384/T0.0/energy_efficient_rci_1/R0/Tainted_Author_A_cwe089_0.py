from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title")  # Get the title from the request's parameters
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute(
        "SELECT content FROM posts WHERE title=?", (title,)
    )  # Execute SQL query to fetch post with given title
    result = cursor.fetchone()  # Fetch the result
    if result:  # If a post was found
        return jsonify(content=result["content"])  # Return the post's content as JSON
    else:  # If no post was found with the given title
        return jsonify(
            {"error": "Post not found"}
        ), 404  # Return an error message and HTTP status code 404 (Not Found)
