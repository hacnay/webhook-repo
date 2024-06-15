from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# MongoDB Atlas connection string
client = MongoClient(os.getenv('MONGO_URI'))
db = client['github_events']
collection = db['events']

@app.route('/webhook', methods=['POST'])
def webhook():
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

    collection.insert_one(event)
    return jsonify({"msg": "Event received"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find({}, {'_id': False}).sort('timestamp', -1).limit(10))
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
