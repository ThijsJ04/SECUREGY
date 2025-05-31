from flask import jsonify
import sqlite3

@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    if not title:
        return "Error: Missing 'title' parameter.", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM Posts WHERE title=?", (title,))
    post = cursor.fetchone()
    if not post:
        return "Error: No post found with that title.", 404

    result = post['content']
    conn.close()
    return jsonify({'content': result})