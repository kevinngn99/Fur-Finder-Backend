from keras_preprocessing.image import load_img, img_to_array, np
from tensorflow.python.keras.models import load_model
import shutil
import requests

url = 'https://images.pexels.com/photos/1170986/pexels-photo-1170986.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
url=input("Enter image URL:")
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response



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


#loads the trained model
model = load_model("cat_dog_model")
perdiction = model.predict(load_image("img.png"))

if perdiction[0][1] > 0.5:
    print("Prediction: Dog")
else:
    print("Prediction: Cat")
print("Probability: ", perdiction)

print("\n")









