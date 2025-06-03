import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_post():
    title = request.args.get("title")  # get the title from the request parameters

    conn = get_db_connection()  # connect to the database using a function
    cur = conn.cursor()
    query = f"SELECT content FROM posts WHERE title = '{title}';"
    cur.execute(query)
    row = cur.fetchone()
    conn.close()  # close the database connection after querying
    if row:  # check if there is a match for the title
        return str(row[0])  # return the content of the post with the matching title
    else:
        return "Post not found"  # return an error message if no match is found
