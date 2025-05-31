from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT content FROM posts WHERE title=?"
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    if result is not None:
        content = result['content']
        return jsonify({'content': content})
    else:
        return jsonify({'error': 'Post not found.'}), 404