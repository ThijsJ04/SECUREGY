import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get database connection
def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# GET /get_post (with title)
@app.route('/get_post', methods=['GET'])
def get_post():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content as JSON.
    '''
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Title is required."}), 400

    try:
        conn = get_db_connection()
        query = """SELECT * FROM posts WHERE title=?"""
        post = conn.execute(query, (title,) )
        data = [post.fetchone()]
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

    return jsonify(data=[row for row in data])