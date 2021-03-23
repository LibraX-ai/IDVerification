"""
    Tutorial can be found at https://github.com/LibraX-ai/IDVerification
"""
import os, requests, base64, json
import requests

subscription_key = "Get Your Key at Dev.LibraX.ai"
assert subscription_key

# Path of the ID image you wish to test ID verification on
FilePath = 'Your ID Photo'

MainURL = "https://api.librax.ai"
TargetURL  = MainURL+"/id/verify"

ENCODING = 'utf-8'
HEADER= {"Ocp-Apim-Subscription-Key": subscription_key,
'Content-Type': 'application/json'}

filename = os.path.basename(FilePath)
image_file = open(FilePath, "rb")
# Base-64 encoding
with open(FilePath, "rb") as image_file:
    encoded_string  = base64.b64encode(image_file.read()).decode(ENCODING) 

# FirstName, LastName and ID Photo should be present in the request body
payload_data = json.dumps({
    "IDPhoto": encoded_string,
    "LastName": "Smith",
    "FirstName": "Adam"
})

response = requests.request("POST", url=TargetURL, data=payload_data, headers=HEADER, stream=True)
response.json()
