from flask import jsonify
import sqlite3

@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT content FROM posts WHERE title=?", (title,))
    result = cur.fetchone()
    if result:
        return jsonify(result['content'])
    else:
        return "Post not found.", 404