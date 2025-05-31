@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get("title")

    with get_db_connection() as conn:
        cur = conn.cursor()
        query = "SELECT * FROM posts WHERE title=?"
        cur.execute(query, (title,))
        result = cur.fetchone()

    if result is None:
        return 'Post not found.'
    else:
        post_content = str(result[1])
        return {'post': post_content}