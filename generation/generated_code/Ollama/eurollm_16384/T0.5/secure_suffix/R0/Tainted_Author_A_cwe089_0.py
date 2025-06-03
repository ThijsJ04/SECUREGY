import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    title = request.args.get("title")  # Get the title from the query string parameters
    query = "SELECT content FROM posts WHERE title = ?"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        query, (title,)
    )  # Execute the SQL query with the title as a parameter
    result = cursor.fetchone()  # Fetch one row of the result
    content = result[0] if result else None  # Get the post's content from the result
    conn.close()
    return content
