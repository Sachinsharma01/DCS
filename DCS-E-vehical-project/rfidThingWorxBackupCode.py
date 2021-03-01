import time
import json
import requests
from mfrc522 import SimpleMFRC522

# Config items
TWX_SERVER = "localhost"
TWX_THINGNAME = "ExampleThing"
TWX_APPKEY = ""
read = SimpleMFRC522()

# Setup the Rest API connection properties
api_endpoint = 'https://' + TWX_SERVER + '/Thingworx/Things/' + TWX_THINGNAME + '/Properties/UID'
api_headers= { 'Content-Type': 'application/json', 'appKey': TWX_APPKEY }

while True:
    id, text = read.read()
    payload = {'UID': id }
    print(id)

    # in a production environment, the SSL certificate should be verified -- there will be warnings about this on the logger
    response = requests.put(api_endpoint, headers=api_headers, json=payload, verify=False)

    # if there's a problem, this will print out the error and quit
    response.raise_for_status()

    time.sleep(10)
