from bs4 import BeautifulSoup
import requests
import urllib.parse
import re
import json

def get_key(num):
    return 'gvOrgPets_lblStatusDesc_' + str(num)

def helpinglostpets():
    url = 'https://www.helpinglostpets.com/v2/OrgPet.aspx?oid=669'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    form = soup.find('form')
    fields = soup.findAll('input')
    formdata = dict((field.get('name'), field.get('value')) for field in fields)
    formdata['__EVENTTARGET'] = 'ddlStatus'
    formdata['__EVENTARGUMENT'] = ''
    formdata['__LASTFOCUS'] = ''
    formdata['ddlStatus'] = '2'
    formdata['ddlSpecies'] = ''
    formdata['ddlGender'] = ''
    formdata['ddlAges'] = '0'
    formdata['txtColor'] = ''
    formdata['ddlProvince'] = '- All -'
    formdata['chkShow1Org'] = 'on'
    formdata['ddlRank'] = 'helpid'
    formdata['ddlPageSize'] = '100'
    formdata['hiddenInputToUpdateATBuffer_CommonToolkitScripts'] = '0'

    postURL = urllib.parse.urljoin(url, form['action'])
    soup = BeautifulSoup(requests.post(postURL, data=formdata).text, 'lxml')

    num = 0

    while (status := soup.find('span', {'id': get_key(num)})) != None:
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

        print('----------------')
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

        num += 1

        myjson = {
                "name": name,
                "gender": gender.text,
                "age": age.text,
                "breed": re.sub('[^A-Za-z]+', ' ', breed.text),
                "size": size.text,
                "dob": "N/A"
        }
        requests.post(url = 'http://10.2.0.251:8000/api/pets/', json = myjson)