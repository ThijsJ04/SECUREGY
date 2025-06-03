from flask import Flask, request, jsonify
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # Database URI
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route("/get_post", methods=["GET"])
def get_post():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get("title")  # Get the title from the URL query string
    posts = Post.query.filter_by(
        title=title
    ).first()  # Query the database for a post with the given title
    if posts:
        return jsonify({"content": posts.content})  # Return the post's content as JSON
    else:
        return "Post not found", 404
