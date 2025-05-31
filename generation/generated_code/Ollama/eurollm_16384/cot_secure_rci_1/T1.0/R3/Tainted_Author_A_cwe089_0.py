import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    with app.app_context():
        cursor = conn.cursor()
        # Run a script to create the table if it doesn't exist
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT)''')
        except sqlite3.OperationalError as e:
            logging.error('Failed to create table', exc_info=True)
    return conn

@app.route('/get_post')
def get_account():
    try:
        conn = get_db_connection()
        with conn:
            title = request.args.get('title')
            if not title:
                return 'Missing required parameter: title', 400
            cursor.execute('SELECT * FROM posts WHERE title=?', (title,))
            row = cursor.fetchone()
            if not row:
                return 'Post with that title not found', 404
            return str(row) + '\n'  # Return content as plain text
    except sqlite3.Error as e:
        logging.error('Database error:', exc_info=True)
    finally:
        conn.close()