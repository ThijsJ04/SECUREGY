# Import necessary modules and establish a connection to the database
import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route to retrieve a single post by its title
@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')  # Assuming 'title' is a GET parameter in the URL

    if not title:  # Check if 'title' is provided
        return "Error: Missing required parameter 'title'"

    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM posts WHERE title=?", (title,))  # Query the database with the provided title
        row = cur.fetchone()  # Retrieve the first matching row (assuming one record per post)

    if not row:  # Check if a match was found
        return "Error: No posts found for the specified title"

    content = str(row[1]) + '\n' + str(row[2]) # Assuming columns are 0 and 3, respectively
    return "<p>Post Content:</p>" + content  # Return the post content with proper HTML formatting