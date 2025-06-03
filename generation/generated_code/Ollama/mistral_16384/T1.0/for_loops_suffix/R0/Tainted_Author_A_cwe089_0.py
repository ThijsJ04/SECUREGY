from sqlite3 import Row


@app.route("/get_post")
def get_account():
    title = request.args.get("title")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT content FROM posts WHERE title=?", (title,))
    post = cur.fetchone()
    if post:
        return post["content"]
    else:
        return "Post not found.", 404
