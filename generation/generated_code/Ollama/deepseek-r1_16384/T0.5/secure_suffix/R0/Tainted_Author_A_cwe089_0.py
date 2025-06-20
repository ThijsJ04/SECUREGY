import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    title = request.args.get("title", "")

    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM posts WHERE title = ?", (title,))
        post = cursor.fetchall()

        if len(post) == 0:
            return jsonify({"error": "Post not found"}), 404
        elif len(post) > 1:
            return jsonify({"error": "Multiple posts with same title exist"}), 409
        else:
            return jsonify(dict(post[0])), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
