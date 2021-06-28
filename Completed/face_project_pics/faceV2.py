import requests
from datetime import datetime, timedelta
import time
import json
import calendar

def camera_name(uuid, data):
    for value in data['cameraStates']:
        if uuid == value['uuid']:
            return value['name']


def human_time(event):
    event = event/1000
    timestamp = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(event))
    return timestamp

def milliseconds_time():
    human = input("")
    #converts human time to ms. the +25200000 is to get it to local time and not GMT
    ms_time = (calendar.timegm(time.strptime(human, '%Y-%m-%d %H:%M:%S')) * 1000) + 25200000
    return ms_time

def camera_data():
    if __name__ == "__main__":
        #url of the api
        endpoint = "https://api2.rhombussystems.com/api/camera/getMinimalCameraStateList"

        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"

        sess = requests.session()

        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))
        #any parameters
        payload = {
        }

        sess.headers = {
            "x-auth-scheme": "api-token",
            "x-auth-apikey": api_key
        }

        resp = sess.post(endpoint, json=payload,
        verify=False)

        content = resp.content
        data = json.loads(content)
        return data

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
        print("Start Time in YYYY-MM-DD H:MM:SS")
        start = milliseconds_time()
        print("End Time in YYYY-MM-DD H:MM:SS")
        end = milliseconds_time()
        payload = {
            "filter":{"types":["named"]},
            "interval":{
                "end": end,
                "start": start
            }
        }
        print(payload)

        my_list = []
        count = 0
        sess.headers = {
            "x-auth-scheme": "api-token",
            "x-auth-apikey": api_key
        }

        resp = sess.post(endpoint, json=payload,
        verify=False)

        content = resp.content
        data = json.loads(content)

        #print(resp.status_code)
        #organized = json.dumps(resp.json(), indent=2, sort_keys=True)
        #print(organized)
        data_camera = camera_data()
        baseURL = "https://media.rhombussystems.com/media/faces?s3ObjectKey="
        for value in data['faceEvents']:
            timestamp = human_time(value['eventTimestamp'])
            my_list.append(value['faceName'])
            my_list.append(timestamp)
            camera = camera_name(value['deviceUuid'], data_camera)
            my_list.append(camera)
            my_list.append(baseURL + value['thumbnailS3Key'])
            
        for k, v, y, z in [my_list[i: i + 4] for i in range(0, len(my_list), 4)]:
            print({'name': k, 'time': v, 'uuid': y, 'thumb': z})
            count += 1
            print(count, "sightings")
            print('\n')
        print(count, 'total sightings')
        # for k, v in [my_list[i: i + 2] for i in range(0, len(my_list), 2)]:
        #print({'name': k, 'time': v})
main()