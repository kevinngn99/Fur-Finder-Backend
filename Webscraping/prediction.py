from keras_preprocessing.image import load_img, img_to_array, np
from tensorflow.python.keras.models import load_model
import shutil
import urllib.request
import os

import sys
sys.path.append('../')


def getImage(filename):
    with open(filename,'rb')as img:
        print()


def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img


def getPerdiction(model,filename):
    perdiction = model.predict(load_image(filename))
    print(perdiction)
    if perdiction[0][0] >.60 or  perdiction[0][1]>0.60 or perdiction[0][1]+perdiction[0][0]>.52 :
        #print("pet confidence : ",perdiction[0][0] + perdiction[0][1])
        return "is a pet"
    else: return "is not a pet"



#Predictor is built to be called from scrapers/
def predictor(url):
    #print(os.listdir('../'))
    model = load_model("../cat_dog_model")
    getImageFromInternet(url)
    return getPerdiction(model)

#Prediction is NOT built to be called from scrapers/
def prediction(url):
    model = load_model("cat_dog_model")
    getImageFromInternet(url)
    return getPerdiction(model)

def reportPrediction(filename):
    model = load_model(os.path.join(os.path.dirname(__file__), '../Webscraping/cat_dog_model'))
    return getPerdiction(model,filename)

def testLocalImages(filename):
    model = load_model(os.path.join(os.path.dirname(__file__), '../Webscraping/cat_dog_model'))
    return getPerdiction(model, os.path.join(os.path.dirname(__file__), '../media/images/' + filename))
