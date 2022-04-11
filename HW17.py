import json
from typing import Optional
from flask import Flask, request, Response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/tms_sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

events = db.Table("user",
                  db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
                  db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True)
                  )


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    city = db.Column(db.String(20), nullable=False, default="Unknown")
    age = db.Column(db.Integer, nullable=True)
    events = db.relationship("Event", secondary=events, lazy="subquery",
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


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<Event %r>" % self.event_name

    def to_dict(self):
        return {
            "id": self.id,
            "event_name": self.event_name
        }


@app.route("/user/", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(email=data["email"], city=data["city"], age=data["age"])
    db.session.add(user)
    db.session.commit()
    return data


@app.route("/event/", methods=["POST"])
def create_event():
    data = request.get_json()
    event = Event(event_name=data["event_name"])
    db.session.add(event)
    db.session.commit()
    return data


@app.route("/user/<int:user_id>")
def get_user(user_id: int):
    user: Optional[User] = User.query.filter_by(id=user_id).first()
    if user:
        return user.to_dict()
    return Response(status=404)


@app.route("/event/<int:event_id>")
def get_event(event_id: int):
    event: Optional[Event] = Event.query.filter_by(id=event_id).first()
    if event:
        return event.to_dict()
    return Response(status=404)


@app.route("/user/")
def get_all_users():
    all_users = User.query
    dict_users = []
    for user in all_users.all():
        dict_users.append(user.to_dict())

    return Response(json.dumps(dict_users), mimetype='application/json')


@app.route("/user/")
def delete_user(user_id: int):
    db.session.query(User).filter(User.id == user_id).delete()
    db.session.commit()
