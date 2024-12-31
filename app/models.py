from . import db

class VisitorIP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(45), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())
