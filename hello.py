import json
from datetime import datetime
from google.cloud import pubsub


client = pubsub.Client()
topic = client.topic('events')

payload = {
    'header': {
        'event_type': 'TripCompleted',
        'event_timestamp': datetime.utcnow().isoformat() + "Z"
    },
    'trip_id': '19021234'
}

# with open('TripCompleted.json') as data_file:    
#     payload = json.load(data_file)

topic.publish(json.dumps(payload))