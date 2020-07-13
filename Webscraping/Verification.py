import requests
import json
import base64
from prediction import reportPrediction

#to do
#check for profanity in names, breed, location,
#check api/pets if pet has been reported as found
#remove pets that have been reported as found from /api/pets
#update the pet model to have a found boolean
#we probably need to give each pet a unique identifier

#maybe check for valid zipcodes?

#checks if a pet with a certain name exisits in database
def isInBackend(name):

    data = requests.get(url='http://192.168.2.14:8000/api/pets//')
    data = data.json()
    for index in range(len(data)):
        inBackend = False
        if data[index]["name"] == name:
            inBackend = True
            print("Pet name is already in database.")
    return inBackend



def getImage(image_data):
    #https://stackoverflow.com/questions/54660800/python-convert-image-to-json
    image_data = base64.b64decode(image_data)

    with open('img.png', 'wb') as file:
        file.write(image_data)

def main():
    #gets the data from the unverified pet database
    data = requests.get(url='http://192.168.2.14:8000/api/reportedpets//')
    data = data.json()


    for i in range(len(data)):
        getImage( data[i]['image'] )
        predict = reportPrediction()
        #checks to see if the image is a cat/dog and checks for Duplicates before posting
        if predict == 'is a pet' and isInBackend(data[i]["name"])==False:
            requests.post(url='http://192.168.2.14:8000/api/pets//', data=data[i])
        else: print("not a pet!")

if __name__ == '__main__':
    main()


