import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')  # Retrieve the title from query parameters

    query = """SELECT content FROM posts WHERE title = ?"""
    with conn:
        cursor.execute(query, (title,))
        row = cursor.fetchone()

    if row is None:
        return jsonify({'error': 'Post not found'}), 404

    post_content = row[0]  # Retrieve the post's content from the database

    return jsonify(post_content)

if __name__ == "__main__":
    app.run()