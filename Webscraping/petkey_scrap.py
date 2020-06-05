from bs4 import BeautifulSoup
import requests

#Scraper for https://petkey.org

#Links for https://petkey.org/lost-pets/zip/{ENTERED_ZIP}
def get_links_local(links):
    zipcode = input("Enter your zipcode: ")
    zipLink = 'https://petkey.org/lost-pets/zip/' + zipcode +'/'
    
    source = requests.get(zipLink).text
    soup = BeautifulSoup(source, 'lxml')

    for lostPet in soup.find_all('div', class_='pet-inner'):
        src = str(lostPet.b.a)
        link = src.split('"')[1]
        link = f'https://petkey.org{link}'
        links.append(link)

    return links

#Links for https://petkey.org/pet-recovery/lostfoundhome.aspx
def get_links(links):
    source = requests.get('https://petkey.org/pet-recovery/lostfoundhome.aspx').text
    soup = BeautifulSoup(source, 'lxml')

    recentlyLost = soup.find('div', class_='section-blue')
    lostPets = recentlyLost.find('div', class_='small-12 columns')
    for lostPet in lostPets.find_all('a'):
        src = str(lostPet).split("href=")[1]
        link = src.split('"')[1]
        link = f'https://petkey.org{link}'
        links.append(link)
    
    #removes the duplicates
    links = list( dict.fromkeys(links) )
    return links

def get_info(links):
    for link in links:
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')

        #Get the image link
        image_src = str(soup.find(class_="photo")).split(' ')[3]
        image_link = image_src.split('src=')[1]


        pet_table = soup.find('table', class_='pet-table')
        pet_info = {}
        for info in pet_table.find_all('tr'):
            attribute = str(info.text).split('\n')[1]
            key = str(info.text).split('\n')[2]
            pet_info[attribute] = key
        pet_info['image'] = image_link
        print(pet_info)


def main():
    links = []

    #Make this change based on the zipcode
    links = get_links_local(links)

    #recently lost pets
    links = get_links(links)

    #Read the tables from the links
    get_info(links)


if __name__ == "__main__":
    main()