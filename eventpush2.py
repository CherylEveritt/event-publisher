import json
from datetime import datetime
from google.cloud import pubsub


client = pubsub.Client()
topic = client.topic('events')


  
x=19020024 
while x <  19020030:
    with open('TripCompleted2.json') as jsonfile:
        x = x+1
        payload = json.load(jsonfile)
        trip_id = int(payload["trip_id"])
        payload["trip_id"]=str(x)
        payload["header"]["event_timestamp"]=datetime.utcnow().isoformat() + "Z"
        # print("old_trip_id: "+str(trip_id))
        # print("new_trip_value: "+payload["trip_id"])
        # print("new_x"+str(x))
        topic.publish(json.dumps(payload))