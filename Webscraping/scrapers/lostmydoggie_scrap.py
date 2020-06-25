from bs4 import BeautifulSoup
import requests

class LostMyDoggie:
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

    def scrap(self):
        json = []

        #zipcode = input('Enter zip code: ')
        zipcode = '33990'
        url = self.get_url(1, 1, zipcode)
        soup = BeautifulSoup(requests.get(url).text, 'lxml')

        header = soup.find('div', {'class': 'col-lg-12 bg-darkcolor'}).font.text
        count = int(str(header).split(' Lost')[0].split('Showing ')[1])
        #print('Number of lost pets: ', count)
        #print()

        num = 1
        page = 1

        while num <= count:

            for column in soup.find_all('div', {'class': 'col-md-3'}):
                num += 1

                image = 'https://www.lostmydoggie.com/' + column.find('div', {'class': 'image'}).a.img['src']
                info = column.find('div', {'class': 'info'})
                detail = column.find('ul', {'class: ', 'custom no-margin'})

                name = info.h4.text
                status = info.h6.span.font.text
                gender = info.h6.text.split(status)[1].encode('ascii',errors='ignore').decode()[1:]
                location = info.h6.find_next_sibling('h6').find(text=True)
                zc = info.h6.find_next_sibling('h6').text.split(location)[1]
                breed = detail.li.text.split('\n')[0]
                color = detail.li.find_next_sibling('li').text
                date = detail.li.find_next_sibling('li').find_next_sibling('li').text

                #print('----------------')
                #print('Image: ', image)
                #print('Name: ', name)
                #print('Status:', status)
                #print('Gender: ', gender)
                #print('Location: ', location)
                #print('Zip: ', zc)
                #print('Breed: ', breed)
                #print('Color: ', color)
                #print(date)

                dict = {
                    'name': name,
                    'gender': gender,
                    'image': image,
                    'breed': breed,
                    'color': color,
                    'date': date
                }

                json.append(dict)
                
            page += 1
            soup = BeautifulSoup(requests.get(self.get_url(num, page, zipcode)).text, 'lxml')

        return json

#if __name__ == "__main__":
    #scrap = LostMyDoggie()
    #json = scrap.scrap()
    #print(json)
