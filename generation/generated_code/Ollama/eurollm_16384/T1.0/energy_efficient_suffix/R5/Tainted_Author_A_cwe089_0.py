import sqlite3
from flask import request

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
    title = request.args.get("title")  # Assuming GET request has 'title' parameter

    if not title:
        return "Missing required parameter: title", 400

    query = f"SELECT * FROM Posts WHERE title='{title}'"
    conn = get_db_connection()
    result = conn.execute(query).fetchone()

    if not result:  # No records found, return empty list
        return []

    post_dict = {
        "title": str(result[1]),
        "content": str(result[2]),
    }  # Assuming first and third columns are title and content respectively
    return post_dict
