from flask import jsonify
import sqlite3

@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM Posts WHERE title=?", (title,))
    result = cursor.fetchone()
    if result:
        return jsonify(result['content'])
    else:
        return "Post not found.", 404