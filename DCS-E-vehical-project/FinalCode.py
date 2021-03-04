import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from datetime import datetime
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
property4 = "User1"
property5 = "TimeOfUser1"
property6="User2"
property7 = "timeOfUser2"

'''Setup all the GPIO pins for the specific tasks'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led, GPIO.LOW)
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, GPIO.LOW)

'''create an object to read the data from rfid'''
reader = SimpleMFRC522()
uid = 727073640024


'''Url and API key to upload data on Thingworx'''
url = "http://dcs.glaitm.org:7080"
apiKey = "4d22662e-a921-4801-b4f7-cbe1cf4e62e3"
thingName = "191500402_rfid_EV"
headers = {'Content-Type' : 'application/json', 'appKey' : apiKey}

fa = sa =0
listUid = [727073640024,866677247667]
userNames=["Vipin","Sachin","No User"]
while True:
        try:
            index = 2
            t = "null"
            d = "null"
            print("Introduce Your Card:")
            UID, text = reader.read()
            if UID in listUid:
                t = "" + datetime.now().strftime("%I : %M : %S")
                d = "" + datetime.now().strftime("%d/%m/%Y)
                print(UID)
                sa += 1
                print(text)
                GPIO.output(relay, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led, GPIO.HIGH)
                time.sleep(1)
                index=listUid.index(UID)
                
                
            else:
                print(UID)
                fa +=1
                GPIO.output(relay, GPIO.LOW)
                GPIO.output(led, GPIO.LOW)
            payload={property1:UID, property4: userNames[index], property2: fa, property3: sa, property5: t}
            res = requests.put(url+'/Thingworx/Things/'+thingName+'/Properties/*',headers=headers,json=payload,
                                   verify=False)
            time.sleep(2)
        
        except:
                GPIO.cleanup()
