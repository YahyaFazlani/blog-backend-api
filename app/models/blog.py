from app.extensions import db
from dataclasses import dataclass

@dataclass
class Blog(db.Model): 
  id:int = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title:str = db.Column(db.String(150))
  content:str = db.Column(db.Text)
  writer_id:int = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self) -> str:
    return f'<Blog "{self.id}">'
