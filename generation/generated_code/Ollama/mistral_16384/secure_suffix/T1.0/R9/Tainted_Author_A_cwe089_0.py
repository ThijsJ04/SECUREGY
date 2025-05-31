@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)
    if not title:
        return 'Title parameter is required.', 400

    conn = get_db_connection()
    cursor = conn.cursor()
    query = 'SELECT content FROM Posts WHERE title=?'
    cursor.execute(query, (title,))
    post = cursor.fetchone()

    if not post:
        return 'Post with that title was not found.', 404

    conn.close()
    return post['content']