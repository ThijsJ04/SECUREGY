import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')
    if not title:
        return 'Title is required', 400

    # Perform database query to find the post with the specified title
    query = f"SELECT * FROM posts WHERE title='{title}'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()  # Returns the first result, which should be the post content

    if not result:
        return 'Post not found', 404

    return str(result[1]), 200