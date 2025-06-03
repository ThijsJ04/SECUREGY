import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


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
    try:
        query = "SELECT * FROM posts WHERE title=? LIMIT 1;"
        cur = conn.cursor()
        cur.execute(query, (request.args.get("title"),))
        row = cur.fetchone()
        if row:
            return str(row[1])  # Return the post's content as a string
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()
