@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT content FROM posts WHERE title=?"
    cursor.execute(query, (title,))
    post = cursor.fetchone()
    if post:
        return post['content']
    else:
        return "Post not found", 404