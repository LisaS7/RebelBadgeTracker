from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_path = Path.cwd() / 'database' / 'tracker.db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)