import requests
import json
import base64
from prediction import reportPrediction

# pip install profanity 
from profanity import profanity 

#to do
#check api/pets if pet has been reported as found
#remove pets that have been reported as found from /api/pets
#update the pet model to have a found boolean
#we probably need to give each pet a unique identifier
#maybe check for valid zipcodes?

#checks if a pet with a certain name exisits in database
def isInBackend(id):
    data = requests.get(url='http://10.2.0.251:8000/api/pets//')
    data = data.json()
    for index in range(len(data)):
        inBackend = False
        if data[index]["id"] == id:
            inBackend = True
            print("Pet name is already in database.")
    return inBackend

#given a petID will return if pet is still reported as lost
def isLost(id):
    data = requests.get(url='http://192.168.2.14:8000/api/pets//')
    data = data.json()
    for index in range(len(data)):

        if data[index]["id"] == id:
            return data[index]["islost"]



#check for profanity in names, breed, location,
def profanityCheck(data):
    if profanity.contains_profanity( data['name']) == True:
        return True
    if profanity.contains_profanity(data['breed']) == True:
        return True
    if profanity.contains_profanity(data['location']) == True:
        return True
    return False

def getImage(image_data):
    #https://stackoverflow.com/questions/54660800/python-convert-image-to-json
    image_data = base64.b64decode(image_data)

    with open('img.png', 'wb') as file:
        file.write(image_data)

def main():
    
    #gets the data from the unverified pet database
    data = requests.get(url='http://10.2.0.251:8000/api/reportedpets//')
    data = data.json()


    for i in range(len(data)):
        getImage( data[i]['image'] )
        predict = reportPrediction()
        #checks to see if the image is a cat/dog and checks for Duplicates before posting
        if predict == 'is a pet' and isInBackend(data[i]["id"])==False and profanityCheck(data[i]) == False:
            requests.post(url='http://10.2.0.251:8000/api/pets//', data=data[i])
        else: print(data[i]["name"],"not a pet!")

        print("is lost?",isLost(1))

if __name__ == '__main__':
    main()


