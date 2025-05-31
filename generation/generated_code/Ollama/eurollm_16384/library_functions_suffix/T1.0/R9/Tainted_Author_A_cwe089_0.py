import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account(title):
    title = request.args.get('title')
    try:
        conn = get_db_connection()
        query = f"SELECT * FROM posts WHERE title='{title}'"
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if row:
            return str(row[1]) + ' ' + str(row[2])
    except sqlite3.Error as e:
        print('Database error')
        return f'{e}', 500
    finally:
        if conn:
            conn.close()