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




if __name__ == "__main__":
        endpoint = "https://api2.rhombussystems.com/api/video/getTimelapseClips"
        api_key = '9Ts3iQ_HSZGHEqwxZnPKpA'
        sess = requests.session()
        today = datetime.now().replace(microsecond=0, second=0, minute=0)
        end_time = today
        start_time = (end_time - timedelta(days=365))
        payload = {
        }
        sess.headers = {
            "Accept": "application/json",
            "x-auth-scheme": "api-token",
            "Content-Type": "application/json",
            "x-auth-apikey": api_key}
        resp = sess.post(endpoint, json=payload,
                        verify=False)
        order_content = resp.content.decode('utf8')
        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(order_content)
        json.dumps(data, indent=4, sort_keys=True)
        for value in data['timelapseClips']:
            print(value['status']['state'])