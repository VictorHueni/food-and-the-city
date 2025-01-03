from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Configurations for Flask
DATABASE_URI = "postgresql+psycopg2://root:root@localhost:5432/food-and-the-city"

def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
