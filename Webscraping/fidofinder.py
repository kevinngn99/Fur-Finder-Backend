from bs4 import BeautifulSoup
from urllib import  urlopen

#sets url to desired webpage
url="https://www.fidofinder.com"

#downloads webpage
Client=urlopen(url)

html=Client.read()

#closes the Webclient
Client.close()

#uses bs4 to parse the HTML
page_soup =BeautifulSoup(html).prettify()

print (page_soup)



