import json
from models.user import User
from models.event import Event
from typing import Optional

from flask import Flask, request, Response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/tms_sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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
