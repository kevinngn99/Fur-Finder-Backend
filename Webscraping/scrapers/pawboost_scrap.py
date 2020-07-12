from bs4 import BeautifulSoup
import requests

class PawBoostScrap:
    def scrap(self, zipcode_):
        # ask for zipCode
        ZipCode = zipcode_

        # sets url to desired webpage
        url = "https://www.pawboost.com/lost-found-pets/?LfdbFeedStatusForm[zip]: =" + str(ZipCode)+"&lost=1"

        # uses bs4 to parse the HTML
        page_soup = BeautifulSoup(requests.get(url).text,features="lxml")

        containers = page_soup.select("#w0")

        json = []

        for index in range(1,len(containers[0].contents)-1,2):
            city = containers[0].contents[index].div.div.h3.text
            date=containers[0].contents[index].div.p.text
            
            imgURL=containers[0].contents[index].select(" div > div > a > div ")
            imageindex = str(imgURL).index("src=")
            jpgindex=str(imgURL).index("/>")

            age = 'N/A'
            breed = 'N/A'
            color = 'N/A'
            date = 'N/A'
            image = str(imgURL)[imageindex+5:jpgindex][:-1]
            location = city[:-6]
            name = containers[0].contents[index].div.div.h2.text
            name = name.strip()
            pos = name.find('\n')
            gender = name[pos + 1:]
            gender = gender.replace(' ', '')[:-3]
            name = name[:pos].replace(' ', '')
            size = 'N/A'
            detail = containers[0].contents[index].find('span')
            status = detail.text[0] + detail.text.lower()[1:]
            petid = detail.parent.text[13:]
            petid = petid.strip()
            zip = city[-5:]
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

        return json

#if __name__ == "__main__":
    #PawBoostScrap().scrap('33990')