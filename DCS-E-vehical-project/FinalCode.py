import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
import requests
import json
import http.client
http.client.HTTPConnection.debuglevel=1
led = 8
relay = 15
GPIO.setwarnings(False)    # Ignore warning for now

'''Properties'''
property1="UID"
property2 = "FailureAttempts"
property3 = "logInAttempts"
property4 = "userName"
property5 = "timeOfUser1"
property5 = "timeOfUser1"

'''Setup all the GPIO pins for the specific tasks'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led, GPIO.LOW)
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, GPIO.LOW)

'''create an object to read the data from rfid'''
reader = SimpleMFRC522()
uid = 727073640024
listUid = [727073640024]


'''Url and API key to upload data on Thingworx'''
url = "http://dcs.glaitm.org:7080"
apiKey = "796a8733-b7b6-440a-85b5-577b51f31bad"
thingName = "191500402_rfid"
headers = {'Content-Type' : 'application/json', 'appKey' : apiKey}

fa = sa =0
listUid = [727073640024]

while True:
        try:
            print("Introduce Your Card:")
            UID, text = reader.read()
            sleep(2)
            if UID in listUid:
                t = time.time()
                print(UID)
                sa += 1
                print(text)
                GPIO.output(relay, GPIO.HIGH)
                sleep(2)
                GPIO.output(led, GPIO.HIGH)
                sleep(1)
            else:
                print(UID)
                fa +=1
                GPIO.output(relay, GPIO.LOW)
                GPIO.output(led, GPIO.LOW)
            payload={property1:UID, property4: text, property2: fa, property3: sa}
            res = requests.put(url+'/Thingworx/Things/'+thingName+'/Properties/*',headers=headers,json=payload,
                                   verify=False)
        except:
                GPIO.cleanup()
