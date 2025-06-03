from sqlite3 import Error
import re


@app.route("/get_post")
def get_account():
    title = request.args.get("title", None)

    if not title:
        return "Title is required", 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    row = cursor.fetchone()

    if not row:
        return "Post not found", 404

    content = row["content"]
    conn.close()

    return content
