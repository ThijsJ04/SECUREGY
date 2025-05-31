@app.route('/get_post')
def get_account():
    title = request.args.get("title")
    if not title:
        return "Title parameter is required."

    conn = get_db_connection()
    post = conn.execute(f"SELECT * FROM posts WHERE title = '{title}'").fetchone()
    conn.close()
    if not post:
        return "Post not found."

    return f'Post content: {post[1]}'