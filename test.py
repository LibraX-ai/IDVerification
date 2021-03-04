import os, requests, base64, json
import requests
subscription_key = "YourSubscriptionKey"
assert subscription_key
FilePath = 'Your_Image_File'
MainURL = "https://libraxai.azure-api.net/"
TargetURL  = "https://libraxai.azure-api.net/id/verify"

ENCODING = 'utf-8'
HEADER= {"Ocp-Apim-Subscription-Key": subscription_key,
'Content-Type': 'application/json'}

filename = os.path.basename(FilePath)
image_file = open(FilePath, "rb")
# Base-64 encoding
with open(FilePath, "rb") as image_file:
    encoded_string  = base64.b64encode(image_file.read()).decode(ENCODING) 


base64_files = json.dumps({
    'image': encoded_string
})

response = requests.request("POST", url=TargetURL, data=base64_files, headers=HEADER, stream=True)
response.json()




