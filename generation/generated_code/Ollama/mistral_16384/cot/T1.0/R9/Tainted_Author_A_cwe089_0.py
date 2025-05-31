@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM Posts WHERE title=?", (title,))
    post = cursor.fetchone()
    if not post:
        return "Post not found.", 404
    conn.close()
    return post['content']