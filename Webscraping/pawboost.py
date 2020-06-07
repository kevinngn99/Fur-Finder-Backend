from bs4 import BeautifulSoup
import requests

# ask for zipCode
ZipCode = input("enter ZipCode: ")

# sets url to desired webpage
url = "https://www.pawboost.com/lost-found-pets/?LfdbFeedStatusForm[zip]: =" + str(ZipCode)+"&lost=1"



# uses bs4 to parse the HTML
page_soup = BeautifulSoup(requests.get(url).text,features="lxml")

containers = page_soup.select("#w0")


for index in range(1,len(containers[0].contents)-1,2):
    name = containers[0].contents[index].div.div.h2.text
    name=str(name)[25:35]
    city = containers[0].contents[index].div.div.h3.text
    date=containers[0].contents[index].div.p.text
    id=containers[0].contents[index].select(" div > div > div > p:nth-child(4) > small")
    idindex=str(id).find("PET ID:")

    date=date[30:46]
    imgURL=containers[0].contents[index].select(" div > div > a > div ")
    imageindex = str(imgURL).index("src=")
    jpgindex=str(imgURL).index("/>")
    print (name)
    print (city)
    print (date)
    print (str(id)[idindex+8:idindex+15])
    print (str(imgURL)[imageindex+5:jpgindex])


# print (page_soup)
