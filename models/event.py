from ..HW17 import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<Event %r>" % self.event_name

    def to_dict(self):
        return {
            "id": self.id,
            "event_name": self.event_name
        }
