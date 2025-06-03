import sqlite3
from flask import request, jsonify

app = Flask(__name__)

# Create a connection pool with 5 connections
conn_pool = sqlite3.connect("Database/database.db", check_same_thread=False)
conn_pool.row_factory = sqlite3.Row
cursor = conn_pool.cursor()


@app.route("/get_post", methods=["GET"])
def get_account():
    # Get the title from the request's parameters
    title = request.args.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400

    # Execute a SQL query to retrieve the post with the specified title
    cursor.execute(f"""SELECT content FROM posts WHERE title = '{title}'""")
    row = cursor.fetchone()

    if not row:
        return jsonify({"error": "Post not found"}), 404

    post_content = row[0]
    return jsonify(post=post_content)
