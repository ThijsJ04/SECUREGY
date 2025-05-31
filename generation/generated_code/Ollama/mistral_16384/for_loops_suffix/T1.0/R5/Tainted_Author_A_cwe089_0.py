@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT content FROM Post WHERE title=?"
    cursor.execute(query, (title,))
    post = cursor.fetchone()
    cursor.close()
    conn.close()
    if post:
        return post['content']
    else:
        return 'Post not found.'