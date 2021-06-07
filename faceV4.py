import requests
from datetime import datetime, timedelta
import time
import json
import calendar
import csv
import sys
import os

def saving_img(thumbnail, name, count):
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

        with open('Report/' + 'Sighting #' + str(count + 1) + '_' + name + '.jpg', 'wb') as f:
            # write the data
            f.write(content)
            f.close()

def human_time(event):
    event = event/1000
    timestamp = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(event))
    return timestamp

def milliseconds_time(human):
    # converts human time to ms. the +25200000 is to get it to local time and not GMT
    ms_time = (calendar.timegm(time.strptime(human, '%Y-%m-%d~%H:%M:%S')) * 1000) + 25200000
    return ms_time

def camera_data():
    if __name__ == "__main__":
        # url of the api
        endpoint = "https://api2.rhombussystems.com/api/camera/getMinimalCameraStateList"
        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"
        sess = requests.session()
        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))
        # any parameters
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
        # url of the api
        endpoint = "https://api2.rhombussystems.com/api/face/getRecentFaceEventsV2"
        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"
        sess = requests.session()
        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))
        # any parameters
        # print("Start Time in yyyy-mm-dd (0)0:00:00)")
        start = milliseconds_time(sys.argv[1])
        # print("End Time in yyyy-mm-dd (0)0:00:00)")
        end = milliseconds_time(sys.argv[2])
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
        
        count = 0
        baseURL = "https://media.rhombussystems.com/media/faces?s3ObjectKey="
        header = ['Name', 'Date', 'Camera', 'Sighting']
        csv_data = []
        data_camera = camera_data()
        os.mkdir('/Users/earthintern/rhombus-interns/face_project_versions/Report')
        for value in data['faceEvents']:
            timestamp = human_time(value['eventTimestamp'])
            csv_data.append([])
            name = value['faceName']
            csv_data[count].append(name)
            csv_data[count].append(timestamp)
            camera = camera_name(value['deviceUuid'], data_camera)
            csv_data[count].append(camera)
            thumbnail = baseURL + value['thumbnailS3Key']
            saving_img(thumbnail, name, count)
            #csv_data[count].append(baseURL + value['thumbnailS3Key'])
            csv_data[count].append(count + 1)
            count += 1
            
        with open('Report/interns_second.csv', 'w', newline = '') as f:
            writer = csv.writer(f)     # create the csv writer
            writer.writerow(header)    # write the header
            writer.writerows(csv_data) # write the data
main()
