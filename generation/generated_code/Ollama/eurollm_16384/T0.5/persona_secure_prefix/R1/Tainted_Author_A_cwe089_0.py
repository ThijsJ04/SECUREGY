import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    query = "SELECT * FROM posts WHERE title=?"
    result = conn.execute(query, (request.args.get("title"),))
    data = result.fetchone() or None
    conn.close()
    return str(data) if data else "Not found"
