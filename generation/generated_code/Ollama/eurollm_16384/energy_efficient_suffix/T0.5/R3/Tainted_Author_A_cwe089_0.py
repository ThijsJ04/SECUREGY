import sqlite3
from flask import Flask, request

# Create an instance of the Flask application
app = Flask(__name__)

# Define a function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Define a route for getting a post by title
@app.route('/get_post', methods=['GET'])
def get_account():
    """Get the post with a specific title."""
    try:
        # Get the title from the request parameters
        title = request.args.get('title')
        if not title:
            return 'Title is required', 400

        # Connect to the database
        conn = get_db_connection()

        # Execute a query to retrieve the post with the specified title
        query = "SELECT * FROM posts WHERE title = ?"
        cur = conn.cursor()
        cur.execute(query, (title,))
        row = cur.fetchone()

        # Return the post's content if it exists; otherwise return a 404 error
        if row:
            return str(row) + '\n', 200
        else:
            conn.close()
            return "Post not found", 404
    except sqlite3.Error as e:
        print("SQLite error: {}".format(e))
        return "An error occurred", 500

# Run the application on port 5001
if __name__ == '__main__':
    app.run(port=5001)