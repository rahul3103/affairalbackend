import json
from flask import Flask, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS
from model import Users, Event
from peewee import create_model_tables

app = Flask(__name__)
CORS(app)

create_model_tables([Users, Event], fail_silently=True)


@app.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        reg_data = json.loads(request.data)
        try:
            user = Users(**reg_data)
            user.save()
            return json.dumps({'success': True, 'user': user.id}), 200
        except:
            return json.dumps({'success': False}), 400


@app.route('/event', methods=['POST'])
def event():
    if request.method == 'POST':
        eve_data = json.loads(request.data)
        try:
            event = Event(**eve_data)
            event.save()
            return json.dumps({'success': True}), 200
        except:
            return json.dumps({'success': False}), 400


@app.route('/users', methods=['GET'])
def users():
    if request.method == 'GET':
        users = Users.select().order_by(Users.rdate.desc())
        if users:
            return (jsonify(users=[model_to_dict(user) for user in users])), 200
        return json.dumps({'users': {}}), 400


@app.route('/users/<int:id>', methods=['GET'])
def user(id):
    if request.method == 'GET':
        user = Users.select().where(Users.id == id).first()
        if user:
            return (jsonify(user=model_to_dict(user))), 200
        return json.dumps({'user': {}}), 400


@app.route('/events', methods=['GET'])
def events():
    if request.method == 'GET':
        events = Event.select().order_by(Event.edate.desc())
        if events:
            return (jsonify(events=[model_to_dict(event) for event in events])), 200
        return json.dumps({'events': {}}), 400


@app.route('/events/<int:id>', methods=['GET'])
def event_uni(id):
    if request.method == 'GET':
        event = Event.select().where(Event.id == id).first()
        if event:
            return (jsonify(event=model_to_dict(event))), 200
        return json.dumps({'event': {}}), 400


if __name__ == '__main__':
    app.run(debug=True)
