from sqlalchemy import create_engine, bindparam
from sqlalchemy.orm import sessionmaker
import sqlite3

def get_account():
    title = request.args.get('title')
    engine = create_engine('sqlite:///Database/database.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Post).filter_by(title=title)
    post = query.first()
    if post:
        return post.content