from sqlite3 import OperationalError
import re

@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)
    if not title:
        return "Title is required", 400

    conn = get_db_connection()
    try:
        cur = conn.execute("SELECT content FROM Posts WHERE title=?", (title,))
        post = cur.fetchone()
        if not post:
            return "Post not found", 404
        return post['content']
    except OperationalError as e:
        return str(e), 500
    finally:
        conn.close()