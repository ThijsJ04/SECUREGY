import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Create a function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('Database/database.db')
    conn.row_factory = sqlite3.Row  # Return row objects for better readability
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    try:
        # Get the post title from the request parameters
        title = request.args.get('title')

        if not title or len(title) == 0:  # Handle empty input
            return 'No title provided', 400

        with get_db_connection() as conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM posts WHERE title=? LIMIT 1"  # Select the post with matching title
            result = cursor.execute(sql, (title,))

            # Fetch and return the post's content
            post_content = result.fetchone()
            if not post_content:  # Handle empty results
                return 'No post found with that title', 404

            return str(post_content[1])  # Return the content of the first post matching the given title
    except sqlite3.Error as e:
        return f'Database error: {e}', 500