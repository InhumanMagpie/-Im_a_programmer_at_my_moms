import json
from flask import Flask, request, Response

app = Flask(__name__)
users = [
    {
        "name": "Alex",
        "profession": "Teacher",
        "id": 1
    },
    {
        "name": "Ivan",
        "profession": "Gardener",
        "id": 2
    },
    {
        "name": "John",
        "profession": "Driver",
        "id": 3
    },
]


@app.route("/")
@app.route("/index/")
def index():
    return "<b>Index Page</b>"


@app.route('/user/<int:user_id>')
def get_user(user_id: int):
    # return [user for user in users if user["id"] == user_id][0]
    for user in users:
        if user_id == user["id"]:
            return user


@app.route('/user/')
def get_all_users():
    return {"users": users}


@app.route('/user/', methods=["POST"])
def create_user():
    data = request.get_json()
    users.append(data)
    print(data)
    return data


@app.route('/user/<int:user_id>', methods=["DELETE"])
def delete_user(user_id: int):
    global users
    users = [user for user in users if user["id"] != user_id]
    return {"users": users}


@app.route('/user/download', methods=['GET'])
def download():
    return Response(
        json.dumps(users),
        mimetype='application/json',
        headers={'Content-Disposition': 'attachment;filename=users.json'}
    )


if __name__ == '__main__':
    app.run()
