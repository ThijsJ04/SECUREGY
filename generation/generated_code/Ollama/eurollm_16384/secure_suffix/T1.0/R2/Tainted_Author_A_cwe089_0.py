from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Assuming a connection to your SQLite database has already been established here
connection = get_db_connection()
cursor = connection.cursor()

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    try:
        # Get the title from the request's query params
        title = request.args.get('title')

        # SQL query to retrieve a single row with the specified title
        query = "SELECT * FROM posts WHERE title=?"
        cursor.execute(query, (title,))

        # Fetch one row's result
        result = cursor.fetchone()

        if not result:
            return jsonify({"error": "No post found with the specified title."}), 404

        data = {"id": result[1], "title": result[2], "content": result[3]}
        return jsonify(data)
    except sqlite3.Error as e:
        # Handle SQLite connection errors or any other exceptions that might occur
        error_message = f"Error retrieving post from database: {e}"
        return jsonify({"error": error_message}), 500