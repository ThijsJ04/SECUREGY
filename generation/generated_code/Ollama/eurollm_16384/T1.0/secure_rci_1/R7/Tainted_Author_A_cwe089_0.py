import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_post(title):
    try:
        # Establish a connection to the database if it exists; otherwise, create one.
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # SQL query to fetch posts with the specified title
        query = """SELECT content FROM posts WHERE title = ?"""
        cursor.execute(query, (title,))

        # Fetch one row of result (assuming each post has only one row)
        result = cursor.fetchone()
        if not result:
            return "Post not found", 404
        else:
            content = str(
                result[0]
            )  # Get the first column value (content) from the query result
            return content, 200
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return "Database connection error", 500
