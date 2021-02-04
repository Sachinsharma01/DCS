import RPi.GPIO as gp
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
try:
    text = input("Enter the Text : ")
    print("Introduce your Card : ")
    reader.write(text)
    print("Data Written")
finally:
    gp.cleanup()
