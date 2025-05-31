# Import required modules
import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    '''
    Establishes a connection to the database.
    Returns the connection object.
    '''
    conn = sqlite3.connect('database.db')  # Database file name
    conn.row_factory = sqlite3.Row  # Return rows as dictionary objects
    return conn


@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()  # Establish connection to the database using helper function
    try:
        query = "SELECT * FROM posts WHERE title=?"
        cur = conn.cursor()
        cur.execute(query, (request.args.get('title'),))  # Get the title from request parameters and execute query
        row = cur.fetchone()  # Retrieve the post with matching title
        if row:  # If a row is returned, it means we found a match
            return f"Post with title '{request.args.get('title')}': {row[1]}"
    finally:
        conn.close()  # Close the database connection when done