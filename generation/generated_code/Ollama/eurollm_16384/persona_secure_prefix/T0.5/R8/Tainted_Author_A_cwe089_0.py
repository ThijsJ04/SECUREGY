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

        if not title or not isinstance(title, str):
            return jsonify({"error": "Title must be a string"}), 400

        # Establish a connection to the database
        conn = get_db_connection()

        # Execute the SQL query to retrieve the post with the specified title
        query = f"""SELECT content FROM posts WHERE title='{title}'"""
        results = conn.execute(query)

        post = results.fetchone()

        if not post:
            return jsonify({"error": "Post not found"}), 404

        # Return the post's content as a JSON object
        return jsonify({"content": post[0]})
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()