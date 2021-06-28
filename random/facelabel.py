import requests
from datetime import datetime, timedelta
import time
import json

def add_label():
    if __name__ == "__main__":
        #url of the api
        endpoint = "https://api2.rhombussystems.com/api/face/addFaceLabel"

        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"

        sess = requests.session()

        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))
        #runs faceID function to print thumbnail
          #faceID()
        #puts face_ID of picture into variable
          #face_ID = faceID()
        #asks user for to input a label for the person
        label = input("What is the name of this person: ")
        #any parameters
        payload = {
            #"faceIdentifier":face_ID,
            "label":label,
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


def main():
    add_label()

main()