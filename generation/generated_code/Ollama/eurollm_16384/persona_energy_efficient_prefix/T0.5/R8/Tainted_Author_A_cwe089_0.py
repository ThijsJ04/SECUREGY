from flask import jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Title is required."}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return jsonify({"error": "Post not found."}), 404

    post_content = {
        'id': result[1],
        'title': title,
        'content': result[2]
    }

    return jsonify(post_content)