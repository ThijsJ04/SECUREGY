from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
import datetime

db_engine = create_engine('sqlite:///Database/database.db')
db_session = scoped_session(sessionmaker(bind=db_engine))

@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    post = db_session.execute(text("SELECT content FROM posts WHERE title = :title"), {'title': title}).fetchone()
    if not post:
        return "Post not found", 404
    return post.content