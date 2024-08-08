from flask_app import app
from .data import badges, clauses


def load_data(db):
    with app.app_context():
        db.create_all()

        for record in badges.values():
            db.session.add(record)
        db.session.commit()

        for record in clauses:
            db.session.add(record)
        db.session.commit()
