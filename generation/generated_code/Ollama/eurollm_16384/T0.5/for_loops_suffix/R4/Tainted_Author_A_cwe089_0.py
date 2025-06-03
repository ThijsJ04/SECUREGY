from flask import request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    title = request.args.get("title")
    query = "SELECT content FROM posts WHERE title = ?"
    cur = conn.cursor()
    cur.execute(query, (title,))
    row = cur.fetchone()
    if row:
        return str(row[0])
    else:
        return "Post not found."
