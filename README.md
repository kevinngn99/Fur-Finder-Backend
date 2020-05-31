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
IPv4 Address. . . . . . . . . . . : 10.0.0.30
```
9. Go back to WSL and type:
```
python manage.py runserver YOUR_IP_ADDRESS:8000
```
