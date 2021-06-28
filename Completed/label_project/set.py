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

def names():
    names = "Drew, James I, Jawad"
    names = names.replace(", ", ",")
    letter_list = names.split(",")
    print(letter_list)


names()
