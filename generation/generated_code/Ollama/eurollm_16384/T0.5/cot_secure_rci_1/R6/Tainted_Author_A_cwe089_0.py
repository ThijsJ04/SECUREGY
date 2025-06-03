from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    title = request.args.get("title")  # Get the title from the request's parameters
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT content FROM posts WHERE title=?"
            cursor.execute(
                query, (title,)
            )  # Execute the SQL query with the title parameter
            result = cursor.fetchone()[
                0
            ]  # Fetch and return the post's content as a string
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"content": result})
