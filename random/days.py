import requests
from datetime import datetime, timedelta
import time
import json
import calendar
import csv
import sys
import os
import argparse
import itertools
import urllib3

def one():
    days = [21, 23, 17, 17, 45, 34]
    for index, this in enumerate(days):
        for that in days[index+1:]:
            if this == that:
                print(this)
                print(that)
one()