from pyA20.gpio import gpio
from pyA20.gpio import port

import dht
import time
from datetime import date
#from datetime import time
from datetime import datetime

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
print("Time :", t)
#print("hour :", h)
#print("minute :", m)
#print("second :", s)


#valuesToStore = current_date_txt + h+':'+m+ ':' +s+ ';' + "\n"
#print(valuesToStore)

# initialize GPIO
PIN2 = port.PA6
gpio.init()

# read data using pin
instance = dht.DHT(pin=PIN2)
counter = 1
while True:
	print("Reading Instance")
	result = instance.read()
	if result.is_valid():
		print("Temperature: {0:0.1f} C".format(result.temperature))
		print("Humidity: {0:0.1f} %".format(result.humidity))
		valueToStore = current_date_txt +h+':'+m+':'+s+';'+'{0:0.1f}'.format(result.temperature)+';'+'{0:0.1f}'.format(result.humidity)+';'+'\n'
		print(valueToStore)
		break
	time.sleep(2)

f=open("Salon.csv", "a+")
f.write(valueToStore)
f.close()
