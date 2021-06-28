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
                "end": 1622738325389,
                "start": 1622738325385
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

        # print(resp.status_code)
        organized = json.dumps(resp.json(), indent=2, sort_keys=True)
        #print(organized)
        #gets the faceID of the unidentified person
        baseURL = "https://media.rhombussystems.com/media/faces?s3ObjectKey="
        face_ID = data['faceEvents'][0]['faceId']
        #print(face_ID)
        #gets the picture of unidentified person
        thumbnail = baseURL + data['faceEvents'][0]['thumbnailS3Key']
        print(thumbnail)
        return face_ID

def names():
    if __name__ == "__main__":
        #url of the api
        endpoint = "https://api2.rhombussystems.com/api/face/updateFace"

        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"

        sess = requests.session()

        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))
        #any parameters
        faceID()
        face_ID = faceID()
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

        print(resp.status_code)
        organized = json.dumps(resp.json(), indent=2, sort_keys=True)
        #print(organized)


def main():
    names()

main()