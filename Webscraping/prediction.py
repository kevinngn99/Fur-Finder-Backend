from keras_preprocessing.image import load_img, img_to_array, np
from tensorflow.python.keras.models import load_model
import shutil
import urllib.request


def getImageFromInternet(url):
    urllib.request.urlretrieve(url, "img.png")


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


def getPerdiction(model):
    perdiction = model.predict(load_image("img.png"))
    if perdiction[0][1] > 0.5:
        return("Dog")
    elif perdiction[0][0]>0.5:
        return("Cat")

def predictor(url):
    model = load_model("cat_dog_model")
    getImageFromInternet(url)
    return getPerdiction(model)