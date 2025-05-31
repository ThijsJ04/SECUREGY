import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connect to the database if it exists, otherwise create a new one.
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    # Get the title from the request parameters.
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Title is required"}), 400

    # Retrieve the post with the given title.
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
    post = cursor.fetchone()
    if not post:
        return jsonify({"error": "Post not found"}), 404

    # Close the database connection.
    conn.close()

    return jsonify(post)

@app.route('/add_post', methods=['POST'])
def add_post():
    # Get the post data from the request parameters.
    title = request.json['title']
    content = request.json['content']
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    # Insert the post into the database.
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    conn.commit()

    # Close the database connection.
    conn.close()

    return jsonify({"message": "Post added successfully"})

@app.route('/update_post', methods=['PUT'])
def update_post():
    # Get the post data from the request parameters.
    title = request.json['title']
    content = request.json['content']
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    # Update the post in the database.
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE posts SET title=?, content=? WHERE id=?", (title, content, request.json['id']))
    if not cursor.rowcount:
        return jsonify({"error": "Post not found"}), 404
    conn.commit()

    # Close the database connection.
    conn.close()

    return jsonify({"message": "Post updated successfully"})