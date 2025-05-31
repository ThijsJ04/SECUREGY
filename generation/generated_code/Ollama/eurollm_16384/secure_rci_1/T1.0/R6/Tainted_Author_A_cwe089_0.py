import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request parameters.
    Return the post's content.
    '''
    title = request.args.get('title')  # Get the title from query params or form data

    conn = get_db_connection()  # Connect to database
    cursor = conn.cursor()  # Create a cursor object

    query = "SELECT content FROM posts WHERE title = ?"  # Define SQL query with parameterized string
    cursor.execute(query, (title,))  # Execute the query with the specified parameters

    row = cursor.fetchone()  # Fetch one row of data from the last executed statement

    if row:  # If a result is returned
        return str(row[0])  # Return the content as a string
    else:
        return "Post not found", 404  # Return a 404 error if post is not found