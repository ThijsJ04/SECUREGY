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
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')  # Get the title parameter from the URL query string

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM posts WHERE title=?"
    cursor.execute(query, (title,))  # Execute a SQL SELECT query to find the post with the specified title
    result = cursor.fetchone()       # Fetch one row of results from the query

    if result:                        # Check if there's a matching post
        content = result[1]           # Retrieve the post content from the database
    else:
        content = "Post not found."   # Return an error message if no post is found

    conn.close()                      # Close the database connection
    return str(content)               # Return the post content as a string