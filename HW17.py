import json
from typing import Optional

from flask import request, Response

from app import app
from database import db
from models.event import Event
from models.m2m_user_events import M2MUserEvents
from models.user import User


@app.route("/user/", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(email=data["email"], city=data["city"], age=data["age"])
    db.session.add(user)
    db.session.commit()
    return data


@app.route("/sign/", methods=["POST"])
def sign_event():
    data = request.get_json()
    event = M2MUserEvents(user_id=data["user_id"], event_id=data["event_id"])
    db.session.add(event)
    db.session.commit()


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
    all_users = User.query.all()
    dict_users = []
    for user in all_users:
        dict_users.append(user.to_dict())

    return Response(json.dumps(dict_users), mimetype='application/json')


@app.route("/user/")
def delete_user(user_id: int):
    db.session.query(User).filter(User.id == user_id).delete()
    db.session.commit()


if __name__ == '__main__':
    app.run()
