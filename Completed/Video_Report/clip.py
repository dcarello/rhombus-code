import requests
from datetime import datetime, timedelta
import time
import json
import calendar
import csv
import sys
import os
import argparse

def splice():
    if __name__ == "__main__":
        # url of the api
        endpoint = "https://api2.rhombussystems.com/api/video/spliceV2"
        api_key = "9Ts3iQ_HSZGHEqwxZnPKpA"
        sess = requests.session()
        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time =  (end_time - timedelta(days=365))
        # any parameters
        payload = {
            "deviceUuids": ["SdFCcHcOTwa4HcSZ3CpsFQ"],
            "durationSec": 20,
            "title": "Clip",
            "startTimeMillis": 1623772800000
        }
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
        print(organized)

splice()