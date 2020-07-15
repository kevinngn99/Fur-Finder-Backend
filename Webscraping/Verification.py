import requests
import json
import base64
from prediction import reportPrediction
from prediction import getImageFromInternet

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
    inBackend = c.execute("SELECT EXISTS(SELECT 1 FROM FurFinderAPI_pet WHERE id is 1);").fetchall()

    return True if inBackend[0][0] == 1 else False
    conn.close()


# given a petID will return if pet is still reported as lost
def isLost(id):
    # check if pet with Id exisits
    if isInBackend(id) == True:
        conn = sqlite3.connect('../db.sqlite3')
        c = conn.cursor()
        lost = c.execute("SELECT islost FROM FurFinderAPI_pet WHERE petid is " + str(id)).fetchall()
        return True if lost[0][0] == 1 else False
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


# will remove all pets marked as found from api/pets and possibly in the future put it in another database to be
# displayed in the reunited pet section of our app.
def removeFoundPets():

    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    c.execute("DELETE FROM FurFinderAPI_pet WHERE status IS false;")
    conn.commit()
    conn.close()


def main():
    # gets the data from the unverified pet database
    data = requests.get(url='http://192.168.2.8:8000/api/pets//')
    data = data.json()
    #removeFoundPets()
    for i in range(len(data)):

        getImageFromInternet(data[i]['image'])
        predict = reportPrediction()
        # checks to see if the image is a cat/dog, checks for Duplicates and profanity before posting
        if predict == 'is a pet' and isInBackend(data[i]["petid"]) == False and profanityCheck(data[i]) == False:
            requests.post(url='http://192.168.2.8:8000/api/pets//', data=data[i])
        else:
            print(data[i]["name"], "not a pet!")


if __name__ == '__main__':
    main()
