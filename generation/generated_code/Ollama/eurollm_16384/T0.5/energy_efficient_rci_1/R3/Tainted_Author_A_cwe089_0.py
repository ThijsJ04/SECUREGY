import sqlite3
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


# Define the Post model with a title column
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


# Create the Post table if it doesn't exist
with app.app_context():
    Post.metadata.create_all(bind=db.engine)


@app.route("/get_post", methods=["GET"])
def get_account():
    title = request.args.get("title")

    # Retrieve the post with the specified title from your SQLite database
    conn = db.session.query(Post).filter_by(title=title).first()

    if not conn:
        return "No post found", 404

    return {"content": conn.content}
