from sqlite3 import Error
import requests

@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)
    if not title:
        return "Missing 'title' parameter", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    post = cursor.fetchone()

    if not post:
        return "Post with title {} not found".format(title), 404

    conn.close()
    return post['content']