import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
led = 40
relay = 17
GPIO.setwarnings(False)    # Ignore warning for now

'''Setup all the GPIO pins for the specific tasks'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led, GPIO.LOW)
GPIO.setup(relay, GPIO.OUT)

'''create an object to read the data from rfid'''
reader = SimpleMFRC522()
uid = 872589727
while True:
        try:
            id, text = reader.read()
            sleep(2)
            if id == uid:
                GPIO.output(relay, GPIO.HIGH)
                sleep(2)
                GPIO.output(led, GPIO.HIGH)
                sleep(1)
            else:
                GPIO.output(relay, GPIO.LOW)
                GPIO.output(led, GPIO.LOW)
        except:
                GPIO.cleanup()
