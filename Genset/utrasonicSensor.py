import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trigger = 23
echo = 24
redLed = 14
greenLed = 15
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setwarnings(False)

def distance():
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    
    start = time.time()
    stop = time.time()
    
    while GPIO.input(echo) == 0:
        start = time.time()
        
    while GPIO.input(echo) == 1:
        stop = time.time()
        
    return (stop - start)*34300 / 2

def checkLevel(distance):
    nd = 18-distance
    return nd*100/18  if nd*100/18 > 0 else 0
def glowLed(level):
    if(level<=25):
        GPIO.output(redLed,True)
        GPIO.output(greenLed,False)
    else:
        GPIO.output(greenLed,True)
        GPIO.output(redLed,False)    

try:
    while True:
        dist = distance()
        level = (checkLevel(dist))
        print(level)
        glowLed(level)
        time.sleep(1)
except KeybopardInterrupt:
    print("done")
    GPIO.cleanup()
    
