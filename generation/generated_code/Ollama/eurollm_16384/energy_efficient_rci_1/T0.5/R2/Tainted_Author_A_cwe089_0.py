import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')  # Retrieve the post title from the query string parameters
    cursor = conn.cursor()
    query = "SELECT content FROM posts WHERE title = ?"
    cursor.execute(query, (title,))  # Execute a SELECT query to find the post with the given title
    result = cursor.fetchone()[0]  # Retrieve the post content from the database
    return result