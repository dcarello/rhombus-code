import requests
from datetime import datetime, timedelta
import time
import json

def faceID():
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
            "filter":{"types":["other"]},
            "interval":{
                "end": 100000000000000,
                "start": 1
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
        #print(organized)
        #gets the faceID of the unidentified person
        baseURL = "https://media.rhombussystems.com/media/faces?s3ObjectKey="
        for value in data['faceEvents']:
            face_ID = value['faceId']
            thumbnail = baseURL+value['thumbnailS3Key']
            slack(thumbnail)
            names(face_ID)
        #print(face_ID)

def names(face_ID):
    if __name__ == "__main__":
        #url of the api
        endpoint = "https://api2.rhombussystems.com/api/face/updateFace"

        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"

        sess = requests.session()

        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))
        #any parameters
        print("Check Slack for the picture.")
        name_person = input('What is this persons name:')
        payload = {'faceUpdates':[
            {
                'faceIds':[face_ID],
                'name':name_person
            }
        ]}
        print(payload)

        sess.headers = {
            "x-auth-scheme": "api-token",
            "x-auth-apikey": api_key
        }

        resp = sess.post(endpoint, json=payload,
        verify=False)

        content = resp.content
        data = json.loads(content)

        #print(resp.status_code)
        organized = json.dumps(resp.json(), indent=2, sort_keys=True)
        #print(organized)

def slack(thumbnail):
    webhook_url = "https://hooks.slack.com/services/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"
    slack_data = {'text': thumbnail}
    response = requests.post(
        webhook_url, data=  json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )

def main():
    faceID()

main()
#use a for loop for each photo