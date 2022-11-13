import Adafruit_DHT
import time
import urllib
import requests

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
sensor_idx  = 11

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)


url_json    = "http://192.168.0.118:8080/json.htm?type=command&param=udevice&idx="
verbose = 1
#if humidity is not None and temperature is not None:
        #f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
  #  print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
#else:
 #   print("Failed to retrieve data from humidity sensor")

    #time.sleep(30)
 
if humidity > 70:
  HUM_STAT = 3
elif humidity > 30:
  HUM_STAT = 1
else:
  HUM_STAT = 2
    
# use Domoticz JSON url to update
cmd = url_json  + str(sensor_idx) + "&nvalue=0&svalue=" + str(temperature) + ";" + str(humidity) + ";"+ str(HUM_STAT)
hf = urllib.request.urlopen(cmd)
if verbose > 0:
  print('Sensor data: temperature = {0:0.1f}C,  humidity =  {1:0.1f}%'.format(temperature, humidity))
  print('Uploaded to Pi: ' + cmd)
  print('Response: ' + hf.read().decode())
hf.close
