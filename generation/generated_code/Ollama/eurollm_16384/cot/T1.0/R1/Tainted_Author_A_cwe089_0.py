import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    return conn

@app.route('/get_post', methods=['GET'])
def get_account(title):
    try:
        conn = get_db_connection()
        query = f"SELECT content FROM posts WHERE title='{title}'"
        results = conn.execute(query).fetchone()
        if results:
            return str(results[0])  # Return the post's content as a string
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        if conn:
            conn.close()