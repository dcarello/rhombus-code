from os import mkdir, name
import requests
from datetime import datetime, timedelta
import time
import json
import calendar
import csv

def saving_img(thumbnail, name, timestamp):
    if __name__ == "__main__":
        #url of the api
        endpoint = thumbnail

        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"

        sess = requests.session()

        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))


        sess.headers = {
            "x-auth-scheme": "api-token",
            "x-auth-apikey": api_key
        }

        resp = sess.get(endpoint,
        verify=False)

        content = resp.content

        print(resp.status_code)
        with open('images/' + name + '_' + timestamp, 'wb') as f:
            # write the data
            f.write(content)
            f.close()

def human_time(event):
    event = event/1000
    timestamp = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(event))
    return timestamp

def milliseconds_time():
    human = input("")
    #converts human time to ms. the +25200000 is to get it to local time and not GMT
    ms_time = (calendar.timegm(time.strptime(human, '%Y-%m-%d~%H:%M:%S')) * 1000) + 25200000
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

def camera_name(uuid, data):
    for value in data['cameraStates']:
        if uuid == value['uuid']:
            return value['name']

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
        print("Start Time in Year-month-day hour:minute:seconds -> yyyy-mm-dd (0)0:00:00)")
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
        # my_list = []
        count = 0
        baseURL = "https://media.rhombussystems.com/media/faces?s3ObjectKey="
        header = ['name', 'time', 'uuid', 'thumb']
        csv_data = []
        sess.headers = {
            "x-auth-scheme": "api-token",
            "x-auth-apikey": api_key
        }
        resp = sess.post(endpoint, json=payload,
        verify=False)
        content = resp.content
        data = json.loads(content)
        print(resp.status_code)
        # organized = json.dumps(resp.json(), indent=2, sort_keys=True)
        #print(organized)
        data_camera = camera_data()
        for value in data['faceEvents']:
            timestamp = human_time(value['eventTimestamp'])
            csv_data.append([])
            name = value['faceName']
            csv_data[count].append(name)
            csv_data[count].append(timestamp)
            camera = camera_name(value['deviceUuid'], data_camera)
            csv_data[count].append(camera)
            thumbnail = baseURL + value['thumbnailS3Key']
            saving_img(thumbnail, name, timestamp)
            csv_data[count].append(baseURL + value['thumbnailS3Key'])
            count += 1
        with open('interns_new.csv', 'w') as f:
        # create the csv writer
            writer = csv.writer(f)
            # write the header
            writer.writerow(header)
            # write the data
            writer.writerows(csv_data)
        # print(csv_data)
main()