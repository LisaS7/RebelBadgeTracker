from datetime import datetime as dt
from sqlalchemy.ext.hybrid import hybrid_property
from flask_app import db
from flask_app.config import SECTION_COLOURS


class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200))
    section = db.Column(db.String(20), nullable=False)
    book = db.Column(db.Integer)
    rating = db.Column(db.String(20))
    notes = db.Column(db.String(500))
    clauses_required = db.Column(db.Integer)
    complete = db.Column(db.Boolean)
    date = db.Column(db.DateTime)
    is_started = db.Column(db.Boolean)
    is_next = db.Column(db.Boolean)
    is_purchased = db.Column(db.Boolean)

    clauses = db.Relationship("Clause", backref="clause", lazy=True)

    def save_changes(self, data):
        date_str = data.get("date")
        if date_str:
            data["date"] = dt.strptime(date_str, "%Y-%m-%d")

        for field in [
            "rating",
            "notes",
            "complete",
            "date",
            "is_started",
            "is_next",
            "is_purchased",
        ]:
            if field in data:
                setattr(self, field, data[field])
        db.session.commit()

    @hybrid_property
    def completed_clauses(self):
        return sum(
            [
                clause.complete * clause.factor
                for clause in self.clauses
                if clause.complete
            ]
        )

    @hybrid_property
    def percentage(self):
        return self.completed_clauses / self.clauses_required * 100

    @hybrid_property
    def colour(self):
        return SECTION_COLOURS[self.section]

    def __repr__(self):
        return f"<Badge {self.id} - {self.name}>"
