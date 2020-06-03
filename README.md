# Fur-Finder-Backend

Do these steps:
1. Create a folder called 'Backend' on desktop and cd into it from WSL. Then copy and run this:
```
virtualenv -p python3 .
```
2. Then enter this:
```
source bin/activate
```
3. Install Django:
```
pip install django
```
4. Install Django REST framework:
```
pip install djangorestframework
```
5. Install CORS:
```
pip install django-cors-headers
```
6. Clone this repo:
```
git clone https://github.com/kevinngn99/Fur-Finder-Backend.git
```
7. Open command prompt and type:
```
ipconfig
```
8. Look for your IPv4 Address and copy it:
```
IPv4 Address. . . . . . . . . . . : YOUR_IP_ADDRESS
```
9. Open settings.py in the FurFinderSITE folder in a code editor and go to line 129. Replace the ip address there:
```
ALLOWED_HOSTS = ['YOUR_IP_ADDRESS']
```
10. Go back to WSL and cd into Fur-Finder-Backend then type:
```
python manage.py runserver YOUR_IP_ADDRESS:8000
```
11. Open the browser and type in the URL:
```
YOUR_IP_ADDRESS:8000
```
12. install Beautiful Soup 4:
```
pip install beautifulsoup4
```
13. xml Parser:
```
pip install lxml
```
