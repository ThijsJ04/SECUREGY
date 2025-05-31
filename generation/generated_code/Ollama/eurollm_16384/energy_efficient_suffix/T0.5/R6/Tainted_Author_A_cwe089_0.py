import sqlite3
from flask import Flask, request, jsonify

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
    try:
        # Get the title from the request's parameters
        title = request.args.get('title')
        if not title or title == '':
            return jsonify({"error": "Missing required parameter: title"}), 400

        # Connect to the database and execute a query
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
        result = cursor.fetchone()

        # Close the database connection and return the post's content as JSON
        if result:
            return jsonify(result)
        else:
            conn.close()
            return jsonify({"error": "Post not found"}), 404
    except sqlite3.Error as e:
        print("Database error:", str(e))
        return jsonify({"error": "Database error occurred"}), 500