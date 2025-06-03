import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    return conn


@app.route("/get_post", methods=["GET"])
def get_account(title):
    title = request.args.get("title")  # Get the title from the query parameter 'title'
    try:
        with sqlite3.connect("./Database/database.db") as conn:
            cur = conn.cursor()
            # Your SQL query should be in here
            cur.execute(
                "SELECT * FROM posts WHERE title=?", (title,)
            )  # Get the post with a specific title from the 'posts' table
            data = (
                cur.fetchone() if cur.rowcount > 0 else None
            )  # If there is more than one result or no results at all, this will return None
        return (
            jsonify({"data": data})
            if data
            else {"error": "No post found with the specified title"}
        )
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return {"error": "Failed to retrieve post"}
