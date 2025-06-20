import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account(title):
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    try:
        with get_db_connection() as conn:
            query = f"SELECT * FROM posts WHERE title='{title}';"
            cur = conn.cursor()
            cur.execute(query)
            row = cur.fetchone()  # fetch one row if the query is successful
        return str(row)
    except Exception as e:
        print(e)
        return "", 500
