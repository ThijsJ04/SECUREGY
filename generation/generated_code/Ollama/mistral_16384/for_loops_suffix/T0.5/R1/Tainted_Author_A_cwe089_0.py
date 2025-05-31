from sqlite3 import Error
import os

def get_account():
    title = request.args.get('title')

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
        post = cursor.fetchone()
        if post:
            return post['content']
        else:
            return "No post found with that title."
    except Error as e:
        print(e)
        return f"Error: {e}"