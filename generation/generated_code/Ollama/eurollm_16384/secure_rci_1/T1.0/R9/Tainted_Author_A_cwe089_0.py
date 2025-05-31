import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')  # Retrieve the title from the request's parameters
    conn = get_db_connection()  # Establish a connection to the database
    query = '''SELECT * FROM posts WHERE title = ?'''
    rows = conn.execute(query, (title,))  # Execute the SQL query with the provided parameters
    post = rows[0] if rows else None  # Return the first row (post) from the result or a null value if no results were found
    conn.close()  # Close the database connection
    return jsonify(post)  # Return the post's content in JSON format