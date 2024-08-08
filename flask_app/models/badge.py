from sqlalchemy.ext.hybrid import hybrid_property
from flask_app import db


def colour(section):
    match section:
        case "Wellness":
            return "#0da96f"
        case "Global":
            return "#0c618d"
        case "Wild":
            return "#e66310"
        case "Creative":
            return "#80659c"
        case "Self Aware":
            return "#af3752"
        case "Grown Up":
            return "#c6ca51"

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

    clauses = db.Relationship('Clause', backref='clause', lazy=True)

    @hybrid_property
    def completed_clauses(self):
        return sum([clause.complete for clause in self.clauses if clause.complete])

    @hybrid_property
    def percentage(self):
        return self.completed_clauses / self.clauses_required * 100

    def __repr__(self):
        return f'<Badge {self.id} - {self.name}>'
