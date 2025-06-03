import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account(title):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Posts WHERE title = ?", (title,))
    results = cursor.fetchall()
    if len(results) == 0:
        return "No posts found."
    content = results[0]["content"]
    connection.close()
    return content
