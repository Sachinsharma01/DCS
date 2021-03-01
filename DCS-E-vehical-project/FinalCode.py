import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
import requests
import json
import http.client
http.client.HTTPConnection.debuglevel=1
'''led = 40
relay = 17'''
GPIO.setwarnings(False)    # Ignore warning for now

'''Properties'''


'''Setup all the GPIO pins for the specific tasks'''
'''GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led, GPIO.LOW)
GPIO.setup(relay, GPIO.OUT)'''

'''create an object to read the data from rfid'''
reader = SimpleMFRC522()
uid = 1031910267405
property1="UID"

'''Url and API key to upload data on Thingworx'''
url = "http://dcs.glaitm.org:7080"
apiKey = "796a8733-b7b6-440a-85b5-577b51f31bad"
thingName = "191500402_rfid"
headers = {'Content-Type' : 'application/json', 'appKey' : apiKey}
'''payLoad = {'Detection' : 'True'}'''
while True:
        try:
            print("try:")
            UID, text = reader.read()
            sleep(2)
            if UID == uid:
                print(UID)
                payload={property1:UID}
                print("SHOW")
                res = requests.put(url+'/Thingworx/Things/'+thingName+'/Properties/*',headers=headers,json=payload,
                                   verify=False)
                '''GPIO.output(relay, GPIO.HIGH)
                sleep(2)
                GPIO.output(led, GPIO.HIGH)
                sleep(1)'''
            else:
                print("Error")
                '''GPIO.output(relay, GPIO.LOW)
                GPIO.output(led, GPIO.LOW)'''
        except:
                GPIO.cleanup()
