import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_account(conn, title):
    cursor = conn.cursor()
    sql = "SELECT * FROM posts WHERE title=?"
    record = (title,)
    try:
        cursor.execute(sql, record)
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "content": row[1]}
        else:
            abort(404, description="Post not found")
    except sqlite3.Error as e:
        abort(500, description=str(e))
