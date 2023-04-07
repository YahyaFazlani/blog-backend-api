from app.extensions import db
from dataclasses import dataclass


@dataclass
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  firstname = db.Column(db.String(50), nullable=False)
  lastname = db.Column(db.String(50), nullable=False)
  password = db.Column(db.String(256), nullable=False)
  email = db.Column(db.String(70), unique=True)
  blogs = db.relationship("Blog", backref="writer")

  def __repr__(self) -> str:
    return f'<User id={self.id}>'