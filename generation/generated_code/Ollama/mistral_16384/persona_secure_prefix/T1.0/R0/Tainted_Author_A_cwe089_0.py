from sqlalchemy import create_engine, Text, bindparam
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

engine = create_engine('sqlite:///./Database/database.db')

@app.route('/get_post')
def get_account():
    title = request.args.get("title")

    with engine.connect() as connection:
        result = connection.execute(f"SELECT content FROM Post WHERE title = {bindparam('title')}", title=title).fetchone()
        if result is not None:
            return jsonify({'content': str(result.content)})
        else:
            return "Post with given title not found.", 404