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
def get_account(title):
    # Get the post with a specific title from the database
    query = "SELECT * FROM posts WHERE title=?"
    cur = conn.cursor()
    cur.execute(query, (title,))
    post = cur.fetchone()
    if post:
        return str(post)
    else:
        # If no matching record is found, return a 404 error
        return "Not Found", 404
