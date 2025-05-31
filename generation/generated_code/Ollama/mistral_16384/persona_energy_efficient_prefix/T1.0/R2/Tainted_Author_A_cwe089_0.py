@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    post = cursor.fetchone()
    if post is None:
        return "Post not found", 404
    else:
        return post['content']