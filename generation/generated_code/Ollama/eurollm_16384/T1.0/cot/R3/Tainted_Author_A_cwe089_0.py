from flask import Flask, request, jsonify
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.db_uri()
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route("/get_post")
def get_post():
    try:
        post = Post.query.filter_by(title=request.args["title"]).first()
        if not post:
            return jsonify({"error": "Invalid title"}), 400
        data = {"id": post.id, "content": post.content}
        return jsonify(data), 200
    except Exception as e:
        logging.exception("Error fetching post: %s", str(e))
        return jsonify({"error": "Database error"} + str(e)), 500


if __name__ == "__main__":
    db_connection = get_db_connection()
    with app.app_context():
        db.create_all(engine)
    db_connection.close()
