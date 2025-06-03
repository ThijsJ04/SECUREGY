from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///database.db"  # Use SQLite as a starting point
)
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route("/get_post", methods=["GET"])
def get_account():
    if "title" not in request.args:
        return {"error": "Missing title parameter."}, 400
    title = request.args.get("title")
    try:
        post = Post.query.filter_by(title=title).first()
        if post is None:
            return {"message": "Post not found."}, 404
        return {"content": post.content}
    except Exception as e:
        return {"error": str(e)}, 500
