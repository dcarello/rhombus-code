import requests
from datetime import datetime, timedelta
import time
import json
from requests.models import Response

def main():
    if __name__ == "__main__":
        #url of the api
        endpoint = "https://api2.rhombussystems.com/api/face/getRecentFaceEventsV2"

        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"

        sess = requests.session()

        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))
        #any parameters
        payload = {
            "filter":{"types":["named"]},
            "interval":{
                "end": 1623087000000,
                "start": 1623081600000
            }
        }
        print(payload)

        sess.headers = {
            "x-auth-scheme": "api-token",
            "x-auth-apikey": api_key
        }

        resp = sess.post(endpoint, json=payload,
        verify=False)

        content = resp.content
        data = json.loads(content)

        print(resp.status_code)
        organized = json.dumps(resp.json(), indent=2, sort_keys=True)
        print(organized)

        baseURL = "https://media.rhombussystems.com/media/faces?s3ObjectKey="
        for value in data['faceEvents']:
            print(value['faceName'])
            print(value['deviceUuid'])
        #gets the picture of unidentified person
        #thumbnail = baseURL + data['faceEvents']['thumbnailS3Key']
        #print(thumbnail)
        #return face_ID
        #print(face_IDs)

main()