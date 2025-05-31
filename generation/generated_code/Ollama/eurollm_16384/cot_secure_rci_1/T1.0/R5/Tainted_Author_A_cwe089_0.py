import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Database/database.db')
    # Set row_factory to use SQLite table rows instead of dicts
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

    if not title:  # Check if the title is provided in the URL
        return jsonify({"error": "Title is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f'SELECT * FROM posts WHERE title=? LIMIT 1'  # Query the database for a post with the given title
    cursor.execute(query, (title,))  # Execute the query

    row = cursor.fetchone()  # Fetch and store the result of the query
    conn.close()  # Close the database connection when finished

    if not row:  # Check if a post was found
        return jsonify({"error": "Post not found"}), 404

    return jsonify(row)  # Return the first row's content as JSON

if __name__ == '__main__':
    app.run()