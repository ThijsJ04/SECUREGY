@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)
    if not title:
        return "Title is required.", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    post = cursor.fetchone()

    if not post:
        return "Post not found.", 404

    conn.close()
    return post['content']