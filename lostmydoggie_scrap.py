from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.lostmydoggie.com/missing-pets.cfm?startr1=1&page_number=1&petkindid=1&alerttypeid=1,3&zipcode=92603&radius=50&sort=OrderDate').text
soup = BeautifulSoup(source, 'lxml')

header = soup.find('div', {'class': 'col-lg-12 bg-darkcolor'}).font.text
count = str(header).split(' Lost')[0].split('Showing ')[1]
print('Number of lost pets: ' + count)

for column in soup.find_all('div', {'class': 'col-md-3'}):
    image = 'https://www.lostmydoggie.com/' + column.find('div', {'class': 'image'}).a.img['src']
    info = column.find('div', {'class': 'info'})
    detail = column.find('ul', {'class: ', 'custom no-margin'})

    name = info.h4.text
    status = info.h6.span.font.text
    gender = info.h6.text.split(status)[1].split('\xa0')[1]
    location = info.h6.find_next_sibling('h6').find(text=True)
    zc = info.h6.find_next_sibling('h6').text.split(location)[1]
    breed = detail.li.text.split('\n')[0]
    color = detail.li.find_next_sibling('li').text
    date = detail.li.find_next_sibling('li').find_next_sibling('li').text

    print('----------------')
    print('Image: ', image)
    print('Name: ', name)
    print('Status:', status)
    print('Gender: ', gender)
    print('Location: ', location)
    print('Zip: ', zc)
    print('Breed: ', breed)
    print('Color: ', color)
    print(date)