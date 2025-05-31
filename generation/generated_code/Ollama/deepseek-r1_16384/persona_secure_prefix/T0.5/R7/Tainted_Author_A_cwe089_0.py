import sqlite3
from flask import Flask, request, jsonify, render_template
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post')
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    try:
        # Extract title parameter from request
        title = request.args.get('title', '')

        if not title:
            return jsonify({'error': 'Title is required'}), 400

        # Connect to database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Prepare SQL query with proper binding to prevent SQL injection
        cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))

        # Fetch the result
        row = cursor.fetchone()

        if not row:
            return jsonify({'error': 'Post not found'}), 404

        # Return the content as JSON
        return jsonify({'content': str(row['content'])}), 200

    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return jsonify({'error': 'Internal database error'}), 500
    finally:
        cursor.close()
        conn.close()