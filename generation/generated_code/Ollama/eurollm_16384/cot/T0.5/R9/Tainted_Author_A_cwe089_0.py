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
    title = request.args.get('title')  # Get the title from the query string
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM posts WHERE title=?"
    cursor.execute(query, (title,))
    result = cursor.fetchone()  # Fetch the post with the specified title
    conn.close()  # Close the database connection
    return result[1]  # Return the post's content as a string