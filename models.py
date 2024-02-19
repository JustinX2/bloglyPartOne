"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, default='https://www.freeiconspng.com/img/17660')

    def __repr__(self):
        return f'<User {self.id}: {self.first_name} {self.last_name}>'

def connect_db(app):
    db.app = app
    db.init_app(app)
