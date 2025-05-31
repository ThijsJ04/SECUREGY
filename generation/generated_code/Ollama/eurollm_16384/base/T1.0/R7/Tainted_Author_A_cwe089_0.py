import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account(title):
    # Connect to the database and retrieve the post with a specific title
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    sql_query = f"SELECT content FROM posts WHERE title='{title}'"
    cursor.execute(sql_query)
    result = cursor.fetchone()

    # Close the database connection and return the post's content or an empty string if not found
    if result:
        return jsonify({'content': result[0]})
    else:
        return jsonify({'message': 'Post not found'}), 404