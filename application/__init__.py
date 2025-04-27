from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config as c

app = Flask("__name__")
app.config["SQLALCHEMY_DATABASE_URI"] = c.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)
