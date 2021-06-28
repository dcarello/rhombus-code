import requests
from datetime import datetime, timedelta
import time
import json
import calendar
import csv
import sys
import os
import argparse
import urllib3

#to disable warnings for not verifying host
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class tracking:
    def __init__(self, cli_args):
        arg_parser = self.__initalize_argument_parser()
        self.args = arg_parser.parse_args(cli_args)
        self.api_url = "https://api2.rhombussystems.com"
        self.api_sess = requests.session()
        self.api_sess.headers = {
            "Accept": "application/json",
            "x-auth-scheme": "api-token",
            "Content-Type": "application/json",
            "x-auth-apikey": self.args.APIkey}

        self.media_sess = requests.session()
        self.media_sess.headers = {
            "Accept": "application/json",
            "x-auth-scheme": "api-token",
            "Content-Type": "application/json",
            "x-auth-apikey": self.args.APIkey
        }
        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        self.end_time = today
        self.start_time =  (self.end_time - timedelta(days=365))
        self.processed: set[str] = set()

    @staticmethod
    def __initalize_argument_parser():
        parser = argparse.ArgumentParser(
            description="Finds a person and splices together clips from multiple cameras to get their path."
        )

        #aruements avaiable for the user to customize
        parser.add_argument('--APIkey', type=str, help='Get this from your console', default="9Ts3iQ_HSZGHEqwxZnPKpA")
        return parser

    def times(self):
        self.end = int(round(time.time() * 1000))
        self.start = self.end - 80000

    #checks if there was a new alert in the past 10 seconds
    def proceed(self):
        # url of the api
        endpoint = self.api_url + "/api/face/getRecentFaceEventsV2"
        # any parameters
        payload = {
        "filter": {
                #"deviceUuids": [
      #"SdFCcHcOTwa4HcSZ3CpsFQ"],
            "types": ["named"]},
            "interval": {
                "start": self.start,
                "end": self.end
    }
        }
        resp = self.api_sess.post(endpoint, json=payload,
        verify=False)
        content = resp.content
        data = json.loads(content)
        organized = json.dumps(resp.json(), indent=2, sort_keys=True)
        #print(organized)
        for value in data['faceEvents']:
            if value["uuid"] not in self.processed:
                self.processed.add(value["uuid"])
                print(value['deviceUuid'])
                print(value['uuid'])
                print(value['faceId'])
                print(value['pitch'])
                print(value['roll'])
                print(value['yaw'])
                return True
        return False

    def execute(self):
        self.times()
        begin = False
        while self.proceed() == False:
            self.times()
            time.sleep(10)

if __name__ == "__main__":
    engine = tracking(sys.argv[1:])
    engine.execute()
