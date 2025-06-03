import sqlite3
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


extend_app = Flask(__name__, instance_relative_config=True)
db_connect = get_db_connection()
db_url = extend_app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{extend_app.instance_path}/database.db"
)
db_engine = create_engine(db_url)
db_session = scoped_session(sessionmaker(bind=db_engine))


@app.route("/get_post")
def get_account():
    title = request.args.get("title")
    post = db_session.execute(
        text("SELECT content FROM posts WHERE title = :title"), {"title": title}
    ).fetchone()
    return post.content if post else "Post not found"
