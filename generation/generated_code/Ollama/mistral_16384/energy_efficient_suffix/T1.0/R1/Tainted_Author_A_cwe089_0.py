@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)
    if not title:
        return "Missing 'title' parameter", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    query = 'SELECT content FROM posts WHERE title=?'
    cursor.execute(query, (title,))
    post = cursor.fetchone()
    if not post:
        return "Post with that title not found", 404

    conn.close()
    return post['content']