from sqlite3 import Error
import os


def get_account():
    title = request.args.get("title")

    if not title:
        return "Title is required", 400

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
        post = cursor.fetchone()

        if not post:
            return "Post not found", 404

        return post["content"]

    except Error as e:
        db.close()
        return f"Error: {e}", 500

    finally:
        db.close()
