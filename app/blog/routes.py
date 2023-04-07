from app.blog import blog_bp
from flask import jsonify, request, abort
from app.models.blog import Blog
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity


@blog_bp.get("/<int:id>")
def get_blog(id):
  blog = Blog.query.filter_by(id=id).first()

  return jsonify(blog)


@blog_bp.post("/")
@jwt_required()
def create_blog():
  data = request.get_json()
  writer = get_jwt_identity()
  try:
    blog = Blog(title=data.get("title", ""), content=data.get(
        "content", ""), writer_id=writer)
  except (KeyError, TypeError):
    abort(400)

  db.session.add(blog)
  db.session.commit()

  return jsonify(blog)


@blog_bp.patch("/<int:id>")
@jwt_required()
def update_blog(id):
  data = request.get_json()
  blog = Blog.query.filter_by(id=id).first_or_404()

  if not blog:
    abort(404)

  user = get_jwt_identity()
  if user != blog.writer_id:
    abort(401)

  for key in data:
    setattr(blog, key, data.get(key))

  db.session.commit()
  return jsonify(blog)


@blog_bp.delete("/<int:id>")
@jwt_required()
def delete_blog(id):
  blog = Blog.query.filter_by(id=id).first_or_404()

  if not blog:
    abort(404)

  user = get_jwt_identity()
  if user != blog.writer_id:
    abort(401)

  db.session.delete(blog)
  db.session.commit()

  return {}, 200
