import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')  # Get the title parameter from the URL

    query = "SELECT * FROM posts WHERE title=?"
    cursor = conn.execute(query, (title,))
    row = cursor.fetchone()

    if row:
        return jsonify({'content': row[1], 'author': row[2]})  # Return the post's content and author
    else:
        return jsonify({"error": "Post not found"}), 404  # Return an error message if no post is found