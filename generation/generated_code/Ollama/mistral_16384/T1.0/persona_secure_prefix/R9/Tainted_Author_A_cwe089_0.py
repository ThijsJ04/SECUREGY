from sqlite3 import Error
import os


@app.route("/get_post")
def get_account():
    title = request.args.get("title", None)

    if not title:
        return "Missing title parameter", 400

    db_conn = get_db_connection()
    cursor = db_conn.cursor()

    try:
        cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
        result = cursor.fetchone()

        if not result:
            return "Post not found.", 404

        return result["content"]

    except Error as e:
        db_conn.close()
        return f"Error while fetching post: {e}", 500

    finally:
        db_conn.close()
