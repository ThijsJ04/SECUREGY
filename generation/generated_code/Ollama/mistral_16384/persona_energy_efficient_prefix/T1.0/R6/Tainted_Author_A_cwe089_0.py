@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    post = cursor.fetchone()
    cursor.close()
    conn.close()
    if post:
        return post['content']
    else:
        return "Post not found.", 404