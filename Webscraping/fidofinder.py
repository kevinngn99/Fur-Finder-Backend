from bs4 import BeautifulSoup
from urllib import  urlopen

#sets url to desired webpage
url="https://www.fidofinder.com/lost-dogs/"


#downloads webpage
Client=urlopen(url)

html=Client.read()

#closes the Webclient
Client.close()

#uses bs4 to parse the HTML
page_soup =BeautifulSoup(html,"html.parser")

containers= page_soup.findAll("div",{"class":"row section"})



for container in containers:

    #searches the html for the pets info
    names = container.findAll("div",{"class":"profileboxname"})
    cities =container.findAll("div","profilebox")
    dates = container.findAll("div","profileboxdate")

    for index in range(0,len(names)):
        name=names[index].text
        city=cities[index].div.img
        date=dates[index].text
        #breed=
        print("NAME:", name)
        print("CITY:", city)
        print("DATE LOST:", date)

#print (page_soup)



