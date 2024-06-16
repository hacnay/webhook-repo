from flask import Blueprint, request, jsonify, current_app
from datetime import datetime
from app.extensions import mongo

webhook = Blueprint('webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == 'push':
        event = {
            "author": data['pusher']['name'],
            "to_branch": data['ref'].split('/')[-1],
            "timestamp": datetime.utcnow(),
            "event_type": "push"
        }
    elif event_type == 'pull_request':
        if data['action'] == 'closed' and data['pull_request']['merged']:
            event = {
                "author": data['pull_request']['user']['login'],
                "from_branch": data['pull_request']['head']['ref'],
                "to_branch": data['pull_request']['base']['ref'],
                "timestamp": datetime.utcnow(),
                "event_type": "merge"
            }
        else:
            event = {
                "author": data['pull_request']['user']['login'],
                "from_branch": data['pull_request']['head']['ref'],
                "to_branch": data['pull_request']['base']['ref'],
                "timestamp": datetime.utcnow(),
                "event_type": "pull_request"
            }
    else:
        return jsonify({"msg": "Unhandled event type"}), 400

    mongo.db.events.insert_one(event)
    return jsonify({"msg": "Event received"}), 200

@webhook.route('/events', methods=["GET"])
def get_events():
    events = list(mongo.db.events.find({}, {'_id': False}).sort('timestamp', -1).limit(10))
    return jsonify(events)
