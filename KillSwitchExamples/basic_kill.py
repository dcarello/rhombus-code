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
import subprocess as sp


#to disable warnings for not verifying host
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class killSwitch():

    def __init__(self, cli_args):
        arg_parser = self.__initalize_argument_parser()
        self.args = arg_parser.parse_args(cli_args)
#        self.api_url = "https://api2.rhombussystems.com"
#        self.api_sess = requests.session()
#        self.api_sess.headers = {
#            "Accept": "application/json",
#            "x-auth-scheme": "api-token",
#            "Content-Type": "application/json",
#            "x-auth-apikey": self.args.APIkey}

#        self.media_sess = requests.session()
#        self.media_sess.headers = {
#            "Accept": "application/json",
#            "x-auth-scheme": "api-token",
#            "Content-Type": "application/json",
#            "x-auth-apikey": self.args.APIkey}
        
    @staticmethod
    def __initalize_argument_parser():
        parser = argparse.ArgumentParser(
            description= "Kill Swicth")
        #aruements avaiable for the user to customize
        parser.add_argument('-a', '--Alias', type=str, help='What is the alias of the string')
        parser.add_argument('-i', '--Host', type=str, help='What is the host ip of the strip')
        parser.add_argument('Plug', type=int, help='What plug do you want to turn on or off')
        parser.add_argument('Switch', type=str, help='Do you want to turn a plug on or off', choices=('on', 'off'))

        
        
        return parser
    
    def execute(self):
       #data = os.system('kasa discover')
       #print (data)
        if self.args.Host:
            output = sp.getoutput('kasa --strip --host ' + self.args.Host + ' ' + self.args.Switch + ' --index ' + str(self.args.Plug - 1 ))
        elif self.args.Alias:
            output = sp.getoutput('kasa --strip --alias ' + self.args.Alias + ' ' + self.args.Switch + ' --index ' + str(self.args.Plug - 1))
        else:
            print('Please put a host or an alias name.')
            quit()

       #print(output)
       #os.system("python3 python-kasa/devtools/dump_devinfo.py 192.168.1.56")
           



if __name__ == "__main__":
    engine = killSwitch(sys.argv[1:])
    engine.execute()