from flask import jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')  # Get the title from the request parameters
    if not title:
        return jsonify({"error": "Title is required."}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE title=?", (title,))  # Query the database for the post with the given title
    row = cursor.fetchone()  # Fetch the first row of results

    if not row:
        return jsonify({"error": "Post not found."}), 404

    data = {
        'title': row['title'],
        'content': row['content']
    }

    conn.close()  # Close the database connection
    return jsonify(data)