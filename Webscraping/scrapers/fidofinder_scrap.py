import requests
import aiohttp
import asyncio

from bs4 import BeautifulSoup
from datetime import datetime

class FidoFinderScrap:
    async def fetch(self, session, url):
        async with session.get(url) as response:
            assert response.status == 200
            soup = BeautifulSoup(await response.text(), 'lxml')

            description = soup.find('span', {'class': 'description'}).findAll(text=True)

            petid = soup.find('h4', {'id': 'idnumber'}).text[4:]
            age = 'N/A'
            breed = None
            color = None
            format = soup.find('div', {'class': 'row mb-2'}).div.h3.text[:-1][8:]
            date = datetime.strptime(format, '%m/%d/%Y').strftime('%B %d, %Y')
            gender = None
            image = 'https://www.fidofinder.com/image.php?id=' + petid
            location = None
            name = soup.find('h2', {'class': 'name'}).text
            size = 'N/A'
            status = 'Lost'
            zip = None

            if len(description) == 4:
                gender = description[0][:-1]
                color = description[1][:-4]
                breed = 'N/A'
                location = description[2][:-3]
                zip = location[-5:]
                location = location[:-6]

                if '&' in color:
                    color = color[:-1]
                elif '/' in color:
                    pos = color.find('(') - 1
                    color = color[:pos] + color[pos + 1:]
                else:
                    color = color.strip()
            elif len(description) == 5:
                gender = description[0][:-1]
                color = description[1]
                breed = description[2][:-1]
                location = description[3][:-3]
                zip = location[-5:]
                location = location[:-6]
                
                if '&' in color:
                    color = color[:-1]
                elif '/' in color:
                    pos = color.find('(') - 1
                    color = color[:pos] + color[pos + 1:]
                else:
                    color = color.strip()
            elif len(description) == 6:
                gender = description[0][:-1]
                color = description[1]
                breed = description[2] + description[3][:-1]
                location = description[4][:-3]
                zip = location[-5:]
                location = location[:-6]
                
                if '&' in color:
                    color = color[:-1]
                elif '/' in color:
                    pos = color.find('(') - 1
                    color = color[:pos] + color[pos + 1:]
                else:
                    color = color.strip()
            
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
        url = 'https://www.fidofinder.com/lost-dogs/?postal=' + str(zipcode)
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        urls = []
        tasks = []
        
        for profile in soup.find_all('div', {'class': 'profilebox'}):
            petid = profile.a['id'].replace('profile_', '')
            urls.append('https://www.fidofinder.com/dog.php?id=' + petid)

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
    #FidoFinderScrap().scrap(33990)
