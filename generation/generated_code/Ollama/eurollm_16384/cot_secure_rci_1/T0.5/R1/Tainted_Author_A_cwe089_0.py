import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    """Return a database connection to the SQLite database."""
    conn = sqlite3.connect('/path/to/database.db', isolation_level=None)  # Added isolation level for better performance
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get-post')
def get_account():
    """Get the post with a specific title."""
    try:
        conn = get_db_connection()  # Added error handling for connection issues
        query = f'''SELECT * FROM posts WHERE title = ?'''
        params = (request.args.get('title'),)
        with conn:
            cur = conn.cursor()
            cur.execute(query, params)
            row = cur.fetchone()  # Parameterized query to prevent SQL injection
            if row is None:
                return jsonify({"error": "Post not found"}), 404
            post_content = row[1]
        return jsonify(post=post_content)
    except sqlite3.Error as e:  # Added error handling for query execution errors
        print(f"Query execution error: {e}")
        return jsonify({"error": "Database error occurred"}), 500

if __name__ == '__main__':
    app.run()