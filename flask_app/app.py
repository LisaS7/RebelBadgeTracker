from pathlib import Path
from flask_app import app, db
from .database.load_data import load_data

db_path = Path.cwd() / 'database' / 'tracker.db'

if not db_path.exists():
    load_data(db)

if __name__ == '__main__':
    app.run(debug=True)