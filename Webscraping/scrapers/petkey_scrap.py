import requests
import aiohttp
import asyncio

from bs4 import BeautifulSoup
from datetime import datetime

class PetKeyScrap:
    def get_urls(self, zipcode):
        links = []
        zipLink = 'https://petkey.org/lost-pets/zip/' + zipcode +'/'
        
        source = requests.get(zipLink).text
        soup = BeautifulSoup(source, 'lxml')

        for lostPet in soup.find_all('div', class_='pet-inner'):
            src = str(lostPet.b.a)
            link = src.split('"')[1]
            link = f'https://petkey.org{link}'
            links.append(link)

        return links

    async def fetch(self, session, url):
        async with session.get(url) as response:
            assert response.status == 200
            soup = BeautifulSoup(await response.text(), 'lxml')

            image_src = str(soup.find(class_="photo")).split(' ')[3]
            image_link = image_src.split('src=')[1]

            pet_table = soup.find('table', class_='pet-table')
            pet_info = {}

            for info in pet_table.find_all('tr'):
                attribute = str(info.text).split('\n')[1]
                key = str(info.text).split('\n')[2]
                pet_info[attribute] = key

            image_link = image_link.replace("\"","")
            pet_info['image'] = image_link

            age = pet_info['Age ']
            breed = pet_info['Breed ']
            color = pet_info['Coloring ']
            format = soup.find('span', {'style': 'color: green;'}).text
            date = datetime.strptime(format, '%m/%d/%Y').strftime('%B %d, %Y')
            gender = pet_info['Gender ']
            image = pet_info['image']
            location = soup.find('span', {'id': 'MainContent_lblLocation'}).text
            name = pet_info['Pet Name']
            petid = pet_info['Ref # ']
            size = 'N/A'
            status = 'Lost'
            zip = location[-5:]
            location = location[:-6]

            print('----------------')
            print(age)
            print(breed)
            print(color)
            print(date)
            print(gender)
            print(image)
            print(location)
            print(name)
            print(petid)
            print(size)
            print(status)
            print(zip)

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

            return dict

    async def run(self, zipcode):
        urls = self.get_urls(zipcode)
        tasks = []

        async with aiohttp.ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(self.fetch(session, url))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            
            return responses

    def scrap(self, zipcode):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        future = asyncio.ensure_future(self.run(zipcode))
        return loop.run_until_complete(asyncio.gather(future))

#if __name__ == "__main__":
    #PetKeyScrap().scrap('33990')