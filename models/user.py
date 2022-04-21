from .event import Event

from database import db
from .m2m_user_events import M2MUserEvents


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    city = db.Column(db.String(20), nullable=False, default='Unknown')
    age = db.Column(db.Integer, nullable=True)
    events = db.relationship(Event, secondary=M2MUserEvents, lazy='subquery',
                             backref=db.backref("users", lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username

    def to_dict(self):
        return {
            'id': self.id,
            'age': self.age,
            'email': self.email,
            'city': self.city
        }
