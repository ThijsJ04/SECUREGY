import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    # Get the title from the request parameters
    title = request.args.get('title')  # Example: 'test_post'

    if not title:
        return jsonify({"message": "Title is required."}), 400

    # Query the database for posts with the specified title
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))  # Example: (title,)
    rows = cursor.fetchone()
    post_content = rows[0] if rows else None

    conn.close()

    return jsonify({"content": post_content})

if __name__ == '__main__':
    app.run(debug=True)