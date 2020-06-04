from bs4 import BeautifulSoup
import requests
import re

if __name__ == "__main__":
    url = 'https://www.helpinglostpets.com/v2/OrgPet.aspx?oid=669'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    status = soup.find('span', {'id': 'gvOrgPets_lblStatusDesc_0'})
    date = status.find_next_sibling('span')
    location = date.find_next_sibling('span')

    block = status.parent.parent.find_next_sibling('tr')
    image = block.td.div.a['href']

    details = block.td.find_next_sibling('td')
    name = block.b.text
    breed = block.table.find_next_sibling('b')
    gender = breed.find_next_sibling('b')
    age = gender.find_next_sibling('b')
    size = age.find_next_sibling('b')
    color = size.find_next_sibling('b')

    print('Status: ', status.text)
    print('Date: ', re.sub('[.]', ' ', date.text[4:]))
    print('Location: ', location.text[3:])
    print('Image: ', image)
    print('Name: ', name)
    print('Breed: ', re.sub('[^A-Za-z]+', ' ', breed.text))
    print('Gender: ', gender.text)
    print('Age: ', age.text)
    print('Size: ', size.text)
    print('Color: ', color.text)
