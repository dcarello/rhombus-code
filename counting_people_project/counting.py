import requests
from datetime import datetime, timedelta
import time
import json
import calendar
import csv
import sys
import os
import argparse
from requests.sessions import default_headers
import urllib3

#to disable warnings for not verifying host
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class counting:

    def __init__(self, cli_args):
        arg_parser = self.__initialize_argument_parser()
        self.args = arg_parser.parse_args(cli_args)
        self.api_url = "https://api2.rhombussystems.com"
        self.api_sess = requests.session()
        self.api_sess.headers = {
            "x-auth-scheme": "api-token",
            "x-auth-apikey": self.args.APIkey}

        self.media_sess = requests.session()
        self.media_sess.headers = {
            "x-auth-scheme": "api-token",
            "x-auth-apikey": self.args.APIkey}
        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        self.end_time = today
        self.start_time =  (self.end_time - timedelta(days=365))

    @staticmethod
    def __initialize_argument_parser():
        parser = argparse.ArgumentParser(
            description= "Keeps an active count of the people in the area")
        #aruements avaiable for the user to customize
        parser.add_argument('--APIkey', type=str, help='Get this from your console', default= "9Ts3iQ_HSZGHEqwxZnPKpA")
        parser.add_argument('-s', '--startTime', type=str, help='Add the end search time in yyyy-mm-dd~(0)0:00:00 or default to 1 hour before current time')
        parser.add_argument('-c', '--cameraName', type=str, help='Name of camera in the console', default= 'Rhombus HQ - Camera 2')
        return parser

    #gets the api data about the cameras in the console and returns it
    def camera_data(self):
        # url of the api
        endpoint = self.api_url + "/api/camera/getMinimalCameraStateList"
        # any parameters
        payload = {
        }
        resp = self.api_sess.post(endpoint, json=payload,
        verify=False)
        content = resp.content
        data = json.loads(content)
        return data

    #gets the uuid from the camera name
    def uuid_number(self, data_camera):
        for value in data_camera['cameraStates']:
                if self.args.cameraName == value['name']:
                    uuid = value['uuid']
                    return uuid

    def bounding_boxs(self, uuid):
        endpoint = self.api_url + "/api/camera/getFootageBoundingBoxes"
        # any parameters
        payload = {
            "cameraUuid": uuid,
            "duration": 100,
            "startTime": self.start
            }
        resp = self.api_sess.post(endpoint, json=payload,
        verify=False)
        content = resp.content
        data = json.loads(content)
        organized = json.dumps(resp.json(), indent=2, sort_keys=True)
        #print(organized)
        final_list = [event for event in data['footageBoundingBoxes'] if event['a'] == 'MOTION_HUMAN']
        processed: set[str] = set()
        print(final_list)
        for value in final_list:
            if value["objectId"] in processed or value['t'] in processed or value['b'] in processed or value['l'] in processed or value['r'] in processed:
                random = True
            else:
                for event in final_list:
                    if abs(value["t"] - event["t"]) < 50 and abs(value["b"] - event["b"]) < 50 and abs(value["l"] - event["l"]) < 50 and abs(value["r"] - event["r"]) < 50:
                        event["objectId"] = value["objectId"]
                processed.add(event["objectId"])
                processed.add(value["t"])
                processed.add(value["b"])
                processed.add(value["l"])
                processed.add(value["r"])
                print("https://console.rhombussystems.com/devices/cameras/SdFCcHcOTwa4HcSZ3CpsFQ/?t=" + str(value['ts']))
                self.count +=1
                print("There are currently " + str(self.count) + " people in the room.")
                print(processed)
        return

    def execute(self):
        count = 0
        data_camera = self.camera_data()
        uuid = self.uuid_number(data_camera)
        off = False
        while off ==False:
            self.count = 0
            self.start = int(round(time.time() * 1000)) - 60000
            self.bounding_boxs(uuid)
            time.sleep(.1)

if __name__ == "__main__":
    engine = counting(sys.argv[1:])
    engine.execute()