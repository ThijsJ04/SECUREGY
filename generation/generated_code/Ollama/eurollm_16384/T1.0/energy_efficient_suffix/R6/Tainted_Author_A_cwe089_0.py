import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_post():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    try:
        title = request.args.get("title")
        if not title or not isinstance(title, str):
            return jsonify({"error": "Title required and should be a string."}), 400
        conn = get_db_connection()
        cursor = conn.cursor()
        sql_query = "SELECT * FROM posts WHERE title=?"
        cursor.execute(sql_query, (title,))
        result = cursor.fetchone()
        if not result:
            return jsonify({"error": f"Post '{title}' not found."}), 404
        return jsonify(result)
    except Exception as e:
        print("An error occurred: ", str(e))
        return jsonify({"error": "Internal server error."}), 500
