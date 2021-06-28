import requests
from datetime import datetime, timedelta
import time
import json
from requests.models import Response

def counting_people(data):
    #for value in data['faces']:
    #print(value['name'])
    baseURL = "https://media.rhombussystems.com/media/faces?s3ObjectKey="
    count=0
    person = input("Enter a name you want to search for: ")
    for value in data['faces']:
        if value['name'] == person:
            count= count+1
            print(baseURL+value['thumbnailS3Key'])
            
    print(count)

def main():
    if __name__ == "__main__":
        #url of the api
        endpoint = "https://api2.rhombussystems.com/api/face/getFacesV2"

        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"

        sess = requests.session()

        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))
        #any parameters
        payload = {
        
        }
        print(payload)

        sess.headers = {
            "x-auth-scheme": "api-token",
            "x-auth-apikey": api_key
        }

        resp = sess.post(endpoint, json=payload,
        verify=False)
        #puts json into variable
        content = resp.content
        data = json.loads(content)

        print(resp.status_code)

        #organizes the json it returns
        organized = json.dumps(resp.json(), indent=2, sort_keys=True)
        #print(organized)

        #for value in data['faces']:
            #print(value['faceID'])
            #print(value['name'])
        counting_people(data)

main()