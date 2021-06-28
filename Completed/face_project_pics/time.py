import requests
from datetime import datetime, timedelta
import time
import json
import calendar
import csv
import sys
import os
import argparse

def time_convert():
    then=str(datetime.now() - timedelta(hours = 1))
    now=str(datetime.now())
    print(then) 
    print(now)
    then = then.replace(' ', '~')
    then = then[:19]
    now = now.replace(' ','~')
    now = now[:19]
    print(then) 
    print(now)

time_convert()