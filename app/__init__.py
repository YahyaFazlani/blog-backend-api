from flask import Flask

from config import Config
from app.extensions import *


def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  # * Extensions
  db.init_app(app)
  jwt.init_app(app)

  # * Blueprints
  from app.blog import blog_bp
  from app.auth import auth_bp
  app.register_blueprint(blog_bp, url_prefix="/blog/")
  app.register_blueprint(auth_bp, url_prefix="/auth/")

  return app
