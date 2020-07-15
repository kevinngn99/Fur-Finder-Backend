
import requests
import json
import base64
from prediction import reportPrediction

# pip install profanity
from profanity import profanity
import sqlite3





# to do
# remove pets that have been reported as found from /api/pets
# maybe check for valid zipcodes?

# checks if a pet with a certain name exisits in database
def isInBackend(id):

    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    inBackend= c.execute("SELECT EXISTS(SELECT 1 FROM FurFinderAPI_pet WHERE id is "+str(id)+");").fetchall()
    inBackend = True if inBackend[0][0] == 1 else False
    print("inBackend :",inBackend)
    return inBackend
    conn.close()


# given a petID will return if pet is still reported as lost
def isLost(id):


    #check if pet with Id exisits
    if isInBackend(id) == True:
        conn = sqlite3.connect('../db.sqlite3')
        c = conn.cursor()
        lost = c.execute("SELECT islost FROM FurFinderAPI_pet WHERE id is "+str(id)).fetchall()
        lost = True if lost[0][0] == 1 else False
        print("lost? :", lost)
        return lost
        conn.close()

    else:
        return "Error pet not in database"





# check for profanity in names, breed, location,
def profanityCheck(data):
    if profanity.contains_profanity(data['name']) == True:
        return True
    if profanity.contains_profanity(data['breed']) == True:
        return True
    if profanity.contains_profanity(data['location']) == True:
        return True
    return False


def getImage(image_data):
    # https://stackoverflow.com/questions/54660800/python-convert-image-to-json
    image_data = base64.b64decode(image_data)

    with open('img.png', 'wb') as file:
        file.write(image_data)


# given a pet id will remove said pet from api/pets and possibly in the future put it in another database to be
# displayed in the reunited pet section of our app.
def removeFoundPets(id):
    if isLost(id) == False:
        print("TODO: figure out to remove pet instance from api/pets if marked as found ")


def main():
    # gets the data from the unverified pet database
    data = requests.get(url='http://192.168.2.8:8000/api/reportedpets//')
    data = data.json()

    for i in range(len(data)):
        getImage(data[i]['image'])
        predict = reportPrediction()
        # checks to see if the image is a cat/dog, checks for Duplicates and profanity before posting
        if predict == 'is a pet' and isInBackend(data[i]["id"]) == False and profanityCheck(data[i]) == False:
            requests.post(url='http://192.168.2.8:8000/api/pets//', data=data[i])
        else:
            print(data[i]["name"], "not a pet!")


if __name__ == '__main__':
    main()
