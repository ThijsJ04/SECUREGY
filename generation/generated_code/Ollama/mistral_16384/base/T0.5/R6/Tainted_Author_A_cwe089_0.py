from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post')
def get_account():
    title = request.args.get('title')  # Get the title from the request's parameters
    if not title:
        return jsonify({"error": "Title is required"}), 400  # Return an error message if no title provided

    conn = get_db_connection()  # Get a connection to the database
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))  # Select the post's content with the given title
    row = cursor.fetchone()  # Fetch the result

    if not row:
        return jsonify({"error": "Post not found"}), 404  # Return an error message if no such post exists

    conn.close()  # Close the database connection
    return jsonify(row.items()[1])  # Return the post's content