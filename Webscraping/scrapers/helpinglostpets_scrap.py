from bs4 import BeautifulSoup
import requests
import urllib.parse
import re
import json
from uszipcode import SearchEngine

class HelpingLostPetsScrap:
    def get_key(self, num):
        return 'gvOrgPets_lblStatusDesc_' + str(num)

    def form(self, soup, page):
        #to get these forms, inspect website and click network tab, click the one matching website name (usually first one), then scroll all the way down
        
        form = soup.find('form')
        fields = soup.findAll('input')
        formdata = dict((field.get('name'), field.get('value')) for field in fields)
        formdata['__EVENTTARGET'] = 'gvOrgPets'
        formdata['__EVENTARGUMENT'] = 'Page$' + str(page)
        formdata['__LASTFOCUS'] = ''
        formdata['ddlStatus'] = '1'
        formdata['ddlSpecies'] = ''
        formdata['ddlGender'] = ''
        formdata['ddlAges'] = '0'
        formdata['txtColor'] = ''
        formdata['ddlProvince'] = '- All -'
        formdata['chkShow1Org'] = 'on'
        formdata['ddlRank'] = 'helpid'
        formdata['ddlPageSize'] = '50'
        formdata['hiddenInputToUpdateATBuffer_CommonToolkitScripts'] = '0'

        return form, formdata

    def soup(self, url, og_soup, page):
        form, formdata = self.form(og_soup, page)
        postURL = urllib.parse.urljoin(url, form['action'])
        soup = BeautifulSoup(requests.post(postURL, data=formdata).text, 'lxml')

        return soup

    def scrap(self, zc):
        search = SearchEngine(simple_zipcode=True)
        zipcode = search.by_zipcode(zc).to_dict()
        state = zipcode['state']

        states = {
            'AL': 1452,
            'AK': None,
            'AZ': 732,
            'AR': 1558,
            'CA': 2481,
            'CO': 1049,
            'CT': 1255,
            'DE': 1559,
            'FL': 1184,
            'GA': 1183,
            'HI': None,
            'ID': 2200,
            'IL': 188,
            'IN': 1407,
            'IA': 2300,
            'KS': 1640,
            'KY': 1560,
            'LA': 1563,
            'ME': None,
            'MD': 1514,
            'MA': None,
            'MI': 1436,
            'MN': 1270,
            'MS': 1432,
            'MO': 1567,
            'MT': 2021,
            'NE': 2199,
            'NV': 2197,
            'NH': None,
            'NJ': 1406,
            'NM': 2242,
            'NY': 1457,
            'NC': 1661,
            'ND': 1949,
            'OH': 1244,
            'OK': 1437,
            'OR': 2198,
            'PA': 1401,
            'RI': None,
            'SC': 1455,
            'SD': None,
            'TN': 1431,
            'TX': 669,
            'UT': 2201,
            'VT': None,
            'VA': 1641,
            'WA': None,
            'WV': 1662,
            'WI': 200,
            'WY': 2202
        }

        json = []

        if states[state] != None:
            url = 'https://www.helpinglostpets.com/v2/OrgPet.aspx?oid=' + str(states[state])
            og_soup = BeautifulSoup(requests.get(url).text, 'lxml')
            soup = self.soup(url, og_soup, 1)
            length = None
            try:
                cssPager = soup.find('tr', {'class': 'cssPager'}).td.font.table.tr
                length = len(cssPager.find_all('td'))
            except:
                length = 1

            count = 1

            while count <= length:
                num = 0
                status = soup.find('span', {'id': self.get_key(num)})

                while status != None:
                    date = status.find_next_sibling('span')
                    location = date.find_next_sibling('span').text[3:]

                    block = status.parent.parent.find_next_sibling('tr')
                    image = block.td.div.a['href']

                    details = block.td.find_next_sibling('td')
                    name = block.b.text
                    breed = block.table.find_next_sibling('b')
                    gender = breed.find_next_sibling('b')
                    age = gender.find_next_sibling('b')
                    size = age.find_next_sibling('b')
                    color = size.find_next_sibling('b')
                    petid = block.b.find_next_sibling('b')
                    zip = location[-5:]

                    age = age.text
                    breed = re.sub('[^A-Za-z]+', ' ', breed.text)[4:]
                    color = color.text
                    date = re.sub('[.]', ' ', date.text[4:])
                    gender = gender.text
                    image = image
                    location = location[:-6]
                    name = name
                    petid = petid.text
                    size = size.text
                    status = status.text
                    zip = zip

                    #print('----------------')
                    #print(age)
                    #print(breed)
                    #print(color)
                    #print(date)
                    #print(gender)
                    #print(image)
                    #print(location)
                    #print(name)
                    #print(petid)
                    #print(size)
                    #print(status)
                    #print(zip)

                    dictionary = {
                        'age': age,
                        'breed': breed,
                        'color': color,
                        'date': date,
                        'gender': gender,
                        'image': image,
                        'location': location,
                        'name': name,
                        'petid': petid,
                        'size': size,
                        'status': status,
                        'zip': zip
                    }

                    json.append(dictionary)

                    num += 1
                    status = soup.find('span', {'id': self.get_key(num)})
                
                count += 1
                soup = self.soup(url, og_soup, count)

        return json

if __name__ == "__main__":
    HelpingLostPetsScrap().scrap('33990')
