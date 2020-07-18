#Import the predictor function from 'prediction'
from prediction import prediction

#Send a URL to predictor function, it returns 'Dog' or 'Cat'
#url = 'https://petkey.blob.core.windows.net/resource/images/1420000/1422000/1422810_300.jpg'

print(prediction(input("http://192.168.2.8:8000/media/images/corgi_xrzrnBv.jpg")))
