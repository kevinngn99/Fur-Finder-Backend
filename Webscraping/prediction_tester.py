#Import the predictor function from 'prediction'
from prediction import prediction

#Send a URL to predictor function, it returns 'Dog' or 'Cat'
#url = 'https://petkey.blob.core.windows.net/resource/images/1420000/1422000/1422810_300.jpg'
while True:
    print(prediction(input("enter url: ")))
