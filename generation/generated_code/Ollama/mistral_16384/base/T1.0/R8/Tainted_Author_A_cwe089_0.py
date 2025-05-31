 def get_account():
        title = request.args.get('title')
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
        post = cursor.fetchone()
        if post:
            return post['content']
        else:
            return "Post not found."

    ...

The `get_account` function now fetches the specified post's title from the request parameters, connects to the database using the existing `get_db_connection` function, executes a SQL query to retrieve the post's content based on the provided title, and returns the post's content if found; otherwise, it returns "Post not found."