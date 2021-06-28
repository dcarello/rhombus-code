import requests
from datetime import datetime, timedelta
import time
import json
import calendar

def human_time(event):
    event = event/1000
    timestamp = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(event))
    return timestamp

def milliseconds_time():
    human = input("")
    #converts human time to ms. the +25200000 is to get it to local time and not GMT
    ms_time = (calendar.timegm(time.strptime(human, '%Y-%m-%d %H:%M:%S')) * 1000) + 25200000
    return ms_time

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
        print("Start Time in Year-month-day hour:minute:seconds")
        start = milliseconds_time()
        print("End Time in Year-month-day hour:minute:seconds")
        end = milliseconds_time()
        payload = {
            "filter":{"types":["named"]},
            "interval":{
                "end": end,
                "start": start
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

        baseURL = "https://media.rhombussystems.com/media/faces?s3ObjectKey="
        for value in data['faceEvents']:
            print(value['faceName'])
            timestamp = human_time(value['eventTimestamp'])
            print(timestamp)
            print(value['uuid'])
            print(baseURL + value['thumbnailS3Key'])
            print("\n")

main()