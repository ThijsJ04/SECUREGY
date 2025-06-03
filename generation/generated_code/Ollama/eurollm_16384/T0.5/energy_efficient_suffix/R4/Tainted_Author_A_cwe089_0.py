import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    try:
        title = request.args.get("title")  # Get the title from GET parameters
        query = "SELECT * FROM posts WHERE title=?"
        cur = conn.cursor()
        cur.execute(query, (title,))
        row = cur.fetchone()
        if row:  # Check if the post exists
            content = row[1]  # Get the content from the first column of the result
            return {"content": content}
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
