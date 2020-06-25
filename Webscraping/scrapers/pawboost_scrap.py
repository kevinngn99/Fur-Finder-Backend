from bs4 import BeautifulSoup
import requests

class PawBoostScrap:
    def scrap(self, zipcode_):
        # ask for zipCode
        ZipCode = zipcode_

        # sets url to desired webpage
        url = "https://www.pawboost.com/lost-found-pets/?LfdbFeedStatusForm[zip]: =" + str(ZipCode)+"&lost=1"

        # uses bs4 to parse the HTML
        page_soup = BeautifulSoup(requests.get(url).text,features="lxml")

        containers = page_soup.select("#w0")

        json = []

        for index in range(1,len(containers[0].contents)-1,2):
            name = containers[0].contents[index].div.div.h2.text
            breed = containers[0].contents[index].select("div > div > div > h2 > small")
            breed=str(breed)[61:69]+""+str(breed)[93:102]
            name=str(name)[25:35]

            city = containers[0].contents[index].div.div.h3.text
            date=containers[0].contents[index].div.p.text
            id=containers[0].contents[index].select(" div > div > div > p:nth-child(4) > small")
            idindex=str(id).find("PET ID:")

            date=date[30:46]
            imgURL=containers[0].contents[index].select(" div > div > a > div ")
            imageindex = str(imgURL).index("src=")
            jpgindex=str(imgURL).index("/>")
            #print ("Name: ",name)
            #print("Breed: ",breed)
            #print ("City: ",city)
            #print ("Date Lost : ",date)
            #print ("ID : ",str(id)[idindex+8:idindex+15])
            #print ("ImgURL: ",str(imgURL)[imageindex+5:jpgindex])
            #print ("\n")

            dict = {
                'name': name,
                'breed': breed,
                'location': city,
                'date': date,
                'petid': str(id)[idindex+8:idindex+15],
                'image': str(imgURL)[imageindex+5:jpgindex]
            }

            json.append(dict)

        return json

#if __name__ == "__main__":
    #json = PawBoostScrap().scrap('33990')
    #print(json)