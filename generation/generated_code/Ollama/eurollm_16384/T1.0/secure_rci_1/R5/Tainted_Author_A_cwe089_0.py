import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Create a SQLite database and table if they don't exist
conn = sqlite3.connect("./Database/database.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title text, content text)"""
)


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    params = request.args
    title = params.get("title")

    if not title:
        return "Please specify the 'title' parameter", 400

    cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
    row = cursor.fetchone()

    if row is None:
        return "No post found with the specified title", 404

    return str(row[1]) + "\n" + str(row[2]), 200
