from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title")
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute("SELECT content FROM Posts WHERE title=?", (title,))
    post = cursor.fetchone()
    if post:
        return jsonify({"content": post["content"]})
    else:
        return jsonify({"error": "No post found with that title."}), 404
