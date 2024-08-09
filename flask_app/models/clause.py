from datetime import datetime as dt
from flask_app import db
from .badge import Badge


class Clause(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    badge_id = db.Column(db.Integer, db.ForeignKey("badge.id"), nullable=False)
    description = db.Column(db.String(500))
    complete = db.Column(db.Boolean)
    date = db.Column(db.DateTime)

    def __repr__(self):
        badge = Badge.query.filter_by(id=self.badge_id).first()
        return f"<Clause {self.id} - {badge.name} - {self.description}>"

    def save_changes(self, data):
        date_str = data["date"]
        if date_str:
            data["date"] = dt.strptime(date_str, "%Y-%m-%d")
        for field in ["complete", "date"]:
            if field in data:
                setattr(self, field, data[field])
        db.session.commit()
