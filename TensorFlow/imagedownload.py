import requests
import base64

petName=input("Enter pet name: ")
data = requests.get(url='http://192.168.2.15:8000/api/pets//')
data = data.json()
#print(data)
for index in range(len(data)) :
    inBackend=False
    if data[index]["name"]==petName:
        image_data =data[index]["image"]
        image_data = base64.b64decode(image_data)
        inBackend=True

if inBackend==False:
    print(petName," not found")
else:
    with open('img.png', 'wb') as file:
        file.write(image_data)






