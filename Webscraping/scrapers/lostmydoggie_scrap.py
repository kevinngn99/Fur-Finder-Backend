import requests

from bs4 import BeautifulSoup
from datetime import datetime

class LostMyDoggieScrap:
    def get_url(self, n, p, z):
        begin = 'https://www.lostmydoggie.com/missing-pets.cfm?startr1='
        num = n
        mid1 = '&page_number='
        page = p
        mid2 = '&petkindid=1&alerttypeid=1,3&zipcode='
        zipcode = z
        end = '&radius=50&sort=OrderDate'

        url = begin + str(num) + mid1 + str(page) + mid2 + str(zipcode) + end
        return url

    def scrap(self, zipcode):
        json = []

        url = self.get_url(1, 1, zipcode)
        soup = BeautifulSoup(requests.get(url).text, 'lxml')

        header = soup.find('div', {'class': 'col-lg-12 bg-darkcolor'}).font.text
        count = int(str(header).split(' Lost')[0].split('Showing ')[1])
        num = 1
        page = 1

        while num <= count:

            for column in soup.find_all('div', {'class': 'col-md-3'}):
                num += 1

                image = 'https://www.lostmydoggie.com/' + column.find('div', {'class': 'image'}).a.img['src']
                info = column.find('div', {'class': 'info'})
                detail = column.find('ul', {'class: ', 'custom no-margin'})

                name = info.h4.text
                petid = info.p.text[4:]
                status = info.h6.span.font.text
                gender = info.h6.text.split(status)[1].encode('ascii',errors='ignore').decode()[1:][:-4]
                location = info.h6.find_next_sibling('h6').find(text=True)
                zip = info.h6.find_next_sibling('h6').text.split(location)[1]
                breed = detail.li.text.split('\n')[0]
                color = detail.li.find_next_sibling('li').text
                date = detail.li.find_next_sibling('li').find_next_sibling('li').text
                date = date[date.find(' ') + 1:]

                '''
                try:
                    date = datetime.strptime(date, '%m/%d/%Y').strftime('%B %d, %Y')
                except:
                    try:
                        date = datetime.strptime(date, '%m/%d/%y').strftime('%B %d, %Y')
                    except:
                        try:
                            date = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
                        except:
                            date = datetime.strptime(date, '%m-%d-%Y').strftime('%B %d, %Y')
                '''

                age = 'N/A'
                size = 'N/A'

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

                dict = {
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

                json.append(dict)
                
            page += 1
            soup = BeautifulSoup(requests.get(self.get_url(num, page, zipcode)).text, 'lxml')

        return json

#if __name__ == "__main__":
    #LostMyDoggieScrap().scrap('33990')
