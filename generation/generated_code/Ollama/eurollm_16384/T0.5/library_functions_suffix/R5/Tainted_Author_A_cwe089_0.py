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
    title = request.args.get("title")

    # SQL query to select the post with the given title
    sql_query = f"SELECT * FROM posts WHERE title = '{title}';"

    # Execute the query and fetch all rows
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()

    if not rows:
        return "Post not found", 404

    # Convert the fetched row to a dictionary for easier access
    post_data = {
        "id": rows[0]["id"],
        "title": rows[0]["title"],
        "content": rows[0]["content"],
    }

    # Close the database connection
    conn.close()

    return jsonify(post_data)
