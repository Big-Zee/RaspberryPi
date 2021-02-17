#!/usr/bin/python
import sys
import urllib
import requests
import json
from datetime import date
from datetime import time
from datetime import datetime

#parameters
url_json = "http://192.168.0.130/state"

response = ""
verbose = 1
responseJson = ""

current_year_full = datetime.now().strftime('%Y')  # 2018
current_month = datetime.now().strftime('%m') # 02 //This is 0 padded
current_day = datetime.now().strftime('%d')   # 23 //This is also padded

current_date_txt = current_year_full + '-' + current_month + '-' + current_day + ';'
# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")

h = now.strftime("%H")
m = now.strftime("%M")
s = now.strftime("%S")
print("time :", t)
print("hour :", h)
print("minute :", m)
print("second :", s)

cmd = url_json
hf = urllib.request.urlopen(cmd)
response = hf.read().decode()

if verbose > 0:
  print('Request sent: ' + cmd)
  
responseJson = json.loads(response)
pm1 = str(responseJson["air"]["sensors"][0]["value"])
pm25 = str(responseJson["air"]["sensors"][1]["value"])
pm10 = str(responseJson["air"]["sensors"][2]["value"])
print('PM1   value: ' + pm1)
print('PM2.5 value: ' + pm25)
print('PM10  value: ' + pm10)
hf.close

 #(str)today.year+'-'+(str)today.month+'-'+(str)today.day+';'+#
valuesToStore = current_date_txt + h+':'+m+ ':' +s+ ';' + pm1 + ';' + pm25 + ';' + pm10 + '\n'
print(valuesToStore)

f=open("AirState.csv", "a+")
f.write(valuesToStore)
f.close()