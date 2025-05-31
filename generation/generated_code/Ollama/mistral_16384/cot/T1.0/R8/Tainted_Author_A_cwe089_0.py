@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT content FROM Posts WHERE title=?"
    cursor.execute(query, (title,))
    post = cursor.fetchone()
    return post.content if post else "No post found"