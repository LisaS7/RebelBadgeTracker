from flask_app import db
from .badge import Badge


class Clause(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    badge_id = db.Column(db.Integer, db.ForeignKey('badge.id'), nullable=False)
    description = db.Column(db.String(500))
    notes = db.Column(db.String(500))
    complete = db.Column(db.Boolean)
    date = db.Column(db.DateTime)

    def __repr__(self):
        badge = Badge.query.filter_by(id=self.badge_id).first()
        return f'<Clause {self.id} - {badge.name} - {self.description}>'
