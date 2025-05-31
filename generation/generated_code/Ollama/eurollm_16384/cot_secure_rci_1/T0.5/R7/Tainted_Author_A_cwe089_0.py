import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')  # Get the title from the request parameters
    query = f"SELECT content FROM posts WHERE title='{title}'"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()  # Fetch the result as a list of rows

    for row in rows:
        content = row['content']  # Extract the content (assuming 'content' is the column name)
        yield jsonify({"content": content})

    conn.close()