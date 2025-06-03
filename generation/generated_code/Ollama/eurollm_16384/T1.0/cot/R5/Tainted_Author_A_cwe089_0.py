import sqlite3
from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = sqlite3.connect("database.db")


# Create a form to get the post title from the user
class GetPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Get Post")


@app.route("/get_post")
def get_post():
    form = GetPostForm()
    if form.validate_on_submit():
        title = form.title.data
        query = "SELECT content FROM posts WHERE title = ? LIMIT 1"
        conn = db.execute(query, (title,))
        post = next(conn)[0]
        return jsonify({"content": post["content"]})
    else:
        # Render the form with errors
        return render_template("get_post.html", title=form.title.data)


if __name__ == "__main__":
    db.row_factory = sqlite3.Row
    app.run(debug=True, host="0.0.0.0")
