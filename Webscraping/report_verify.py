#https://stackoverflow.com/questions/54660800/python-convert-image-to-json

import requests
import json
import base64
from prediction import reportPrediction

def getImage():
    data = requests.get(url='http://10.2.0.251:8000/api/report/')
    data = data.json()
    image_data = data[0]['image'] 
    image_data = base64.b64decode(image_data)

    with open('img.png', 'wb') as file:
        file.write(image_data)

getImage()
print(reportPrediction())