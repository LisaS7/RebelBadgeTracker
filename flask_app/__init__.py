from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .utils.filters import percentage_format, adjust_colour


app = Flask(__name__)

db_path = Path.cwd() / "database" / "tracker.db"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.jinja_env.filters["percentage_format"] = percentage_format
app.jinja_env.filters["adjust_colour"] = adjust_colour

db = SQLAlchemy(app)

from flask_app.routes import main
