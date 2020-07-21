
from prediction import reportPrediction
from prediction import load_image
from prediction import getImage
from profanity import profanity
import sqlite3

# checks if a pet with that id exists in database
# def isInBackend(id):
#     conn = sqlite3.connect('../db.sqlite3')
#     c = conn.cursor()
#     inBackend = c.execute("SELECT EXISTS(SELECT 1 FROM FurFinderAPI_pet WHERE id is 1);").fetchall()
#     print("inBackend: ",True if inBackend[0][0] == 1 else False)
#     return True if inBackend[0][0] == 1 else False
#     conn.close()


# # given a petID will return if pet is still reported as lost
# def isLost(id):
#     # check if pet with Id exisits
#     if isInBackend(id) == True:
#         conn = sqlite3.connect('../db.sqlite3')
#         c = conn.cursor()
#         lost = c.execute("SELECT islost FROM FurFinderAPI_pet WHERE petid is " + str(id)).fetchall()
#         return True if lost[0][0] == 1 else False
#         conn.close()
#     else:
#         return "Error pet not in database"


#given a pet id remove that Pet
def removePet(id):
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    c.execute("DELETE FROM FurFinderAPI_pet WHERE petid =='"+ str(id) +"';")
    #remove comment to commit to database
    #conn.commit()
    conn.close()


# will remove all pets marked as found from api/pets and possibly in the future put it in another database to be
# displayed in the reunited pet section of our app.
def removeFoundPets():

    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    c.execute("DELETE FROM FurFinderAPI_pet WHERE status =='Found';")
    conn.commit()
    conn.close()

#uses tensorflow to check if image is approved if not then removes it from database
def removeNonPetImage():
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    imageListing=c.execute("SELECT image,id FROM FurFinderAPI_petimage ;").fetchall()

    for i in range(len(imageListing)):
        predict = reportPrediction("../media/"+imageListing[i][0])
        if predict == "is not a pet":
            removePet(imageListing[i][1])
            print(str(imageListing[i][1])+" removed. not a pet ")
        else: print(str(imageListing[i][1])+" not removed because it's a pet")

    #uncomment for database changes to take effect
    #conn.commit()
    conn.close()

#removes all listings of pets where the breed, name, city,and zip contain profanity
def removePetsWithProfanity():
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    petListing = c.execute("SELECT breed,name,city,zip,petid FROM FurFinderAPI_pet ").fetchall()

    for i in range(len(petListing)):
        if profanity.contains_profanity(petListing[i][0]) == True or profanity.contains_profanity(petListing[i][1]) == True or profanity.contains_profanity(petListing[i][2]) == True or profanity.contains_profanity(petListing[i][3]) == True:
           removePet(petListing[i][4])
    conn.commit()
    conn.close()

def main():
    removeFoundPets()
    removeNonPetImage()
    removePetsWithProfanity()


if __name__ == '__main__':
    main()
