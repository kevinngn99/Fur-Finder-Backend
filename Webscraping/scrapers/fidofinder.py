from bs4 import BeautifulSoup
import requests



def fidofind(zipcode_):
    # ask for zipCode
    ZipCode = zipcode_

    # sets url to desired webpage
    url = "https://www.fidofinder.com/lost-dogs/?postal=" + str(ZipCode)


    # uses bs4 to parse the HTML
    page_soup = BeautifulSoup(requests.get(url).text,features="lxml")

    containers = page_soup.findAll("div", {"class": "row section"})

    for container in containers:

        # searches the html for the pets info
        names = container.findAll("div", {"class": "profileboxname"})
        cities = container.findAll("div", "profilebox")

        dates = container.findAll("div", "profileboxdate")

        for index in range(0, len(names)):
            name = names[index].text
            city = cities[index].contents[1].contents[1].contents[0]
            commaIndex = str(city).find(",")  # finds the only comma indicating the state
            inIndex = str(city).index("in")  # finds the word 'in' indicating the start of the state
            date = dates[index].text
            iDIndex = str(cities[index].contents[1]).index("id=")
            ID = str(cities[index].contents[1])[iDIndex + 3:iDIndex + 9]
            imgURL = "https://www.fidofinder.com/image.php?id=" + str(ID) + "&rand=4367"

            print("NAME:", str(name)[1:len(str(name)) - 1])
            print("CITY:", str(city)[inIndex + 2:commaIndex] + ',' + str(city)[commaIndex + 2:commaIndex + 4])
            print("DATE LOST:", str(date)[1:8])
            print ("Breed:", str(city)[14:inIndex - 1])
            print("Status:", " Lost")
            print("ImgUrl:", imgURL)
            print("ID:", ID)
            print ("")

            myjson = {
                "name": str(name)[1:len(str(name)) - 1],
                "gender": "N/A",
                "age": "N/A",
                "breed": str(city)[14:inIndex - 1],
                "size": "N/A",
                "dob": "N/A"
            }
            requests.post(url = 'http://10.2.0.251:8000/api/pets/', json = myjson)
