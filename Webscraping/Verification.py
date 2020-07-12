import requests
import json
import base64
from prediction import reportPrediction

def getImage(image_data):
    #https://stackoverflow.com/questions/54660800/python-convert-image-to-json
    image_data = base64.b64decode(image_data)

    with open('img.png', 'wb') as file:
        file.write(image_data)

def main():
    data = requests.get(url='http://10.2.0.251:8000/api/reportedpets//')
    data = data.json()

    for i in range(len(data)):
        getImage( data[i]['image'] )
        predict = reportPrediction()
        if predict == 'is a pet':
            requests.post(url='http://10.2.0.251:8000/api/pets//', data=data[i])

if __name__ == '__main__':
    main()