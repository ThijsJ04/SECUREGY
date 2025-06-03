import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_post():
    title_param = request.args.get("title")
    if not title_param:
        return jsonify({"error": "Title parameter is required"}), 400

    conn = get_db_connection()
    query = """SELECT content FROM posts WHERE title=?"""
    results = conn.execute(query, (title_param,))
    post_content = results.fetchone()

    if not post_content:
        return jsonify({"error": "Post with the given title not found"}), 404

    content_json = post_content[0]
    conn.close()
    return jsonify(post=content_json), 200
