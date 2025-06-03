import sqlite3
from flask import Flask, request
from functools import wraps

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    # ...
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    try:
        conn = get_db_connection()
        if (
            not "title" in request.args
            or not request.args["title"]
            or not request.args["title"].strip()
        ):
            return "Please provide a valid title."
        query = (
            f"""SELECT * FROM posts WHERE title='{request.args["title"]}' LIMIT 1;"""
        )
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()
    except sqlite3.Error as e:
        return f"Database error occurred: {e}", 500
    finally:
        try:
            conn.close()
        except Exception:
            None
    if (
        not result
        or "content" in request.args
        and request.args["content"]
        and not request.args["content"].strip()
    ):
        return "Please provide a valid content."
    post = dict(result)
    del post["timestamp"]  # Remove the unnecessary timestamp field from the result
    if "content" in request.args:
        post["content"] = request.args["content"]
    return jsonify(post), 200
