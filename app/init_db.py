from app.extensions import db
from app.models.user import User
from app.models.blog import Blog

user1 = User(firstname="Sherlock", lastname="Holmes")
user2 = User(firstname="Jon", lastname="Snow")
user3 = User(firstname="John", lastname="Watson")

blog1 = Blog(title="First blog", content="Some content", writer_id_id=1)
blog2 = Blog(title="Second blog", content="Some content", writer_id_id=user2)
blog3 = Blog(title="Third blog", content="Some content", writer_id_id=user3)
blog4 = Blog(title="Fourth blog", content="Some content", writer_id_id=user1)

db.session.add_all([user1, user2, user3])
db.session.add_all([blog1, blog2, blog3, blog4])

db.session.commit()
