from database import db


class M2MUserEvents(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), primary_key=True)
