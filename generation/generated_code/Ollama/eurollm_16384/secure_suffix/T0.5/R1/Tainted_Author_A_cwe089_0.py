import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')  # Create a connection to the database
    return conn


@app.route('/get_post', methods=['GET'])
def get_account(title):
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()  # Get the database connection
    cursor = conn.cursor()
    sql = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(sql, (title,))  # Execute a query with parameters
    result = cursor.fetchone()  # Fetch the result of the query
    conn.close()  # Close the database connection when done
    return str(result[0]) if result else "Post not found"