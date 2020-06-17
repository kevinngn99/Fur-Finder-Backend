import os

import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub  # can pip install
from keras_preprocessing.image import load_img, img_to_array, np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# load and prepare the image
from tensorflow.python.keras.models import load_model


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


# for plotting images (optional)
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()


# getting data
_URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'

path_to_zip = tf.keras.utils.get_file('cats_and_dogs.zip', origin=_URL, extract=True)

PATH = os.path.join(os.path.dirname(path_to_zip), 'cats_and_dogs_filtered')

base_dir = PATH
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

train_cats = os.path.join(train_dir, 'cats')
train_dogs = os.path.join(train_dir, 'dogs')
validation_cats = os.path.join(validation_dir, 'cats')
validation_dogs = os.path.join(validation_dir, 'dogs')

num_cats_tr = len(os.listdir(train_cats))
num_dogs_tr = len(os.listdir(train_dogs))
num_cats_val = len(os.listdir(validation_cats))
num_dogs_val = len(os.listdir(validation_dogs))

total_train = num_cats_tr + num_dogs_tr
total_val = num_cats_val + num_dogs_val

BATCH_SIZE = 5
IMG_SHAPE = 224  # match image dimension to mobile net input

# generators

# prevent memorization
train_image_generator = ImageDataGenerator(
    rescale=1. / 255
)

validation_image_generator = ImageDataGenerator(
    rescale=1. / 255)

train_data_gen = train_image_generator.flow_from_directory(batch_size=BATCH_SIZE,
                                                           directory=train_dir,
                                                           shuffle=True,
                                                           target_size=(IMG_SHAPE, IMG_SHAPE),
                                                           class_mode='binary')

val_data_gen = train_image_generator.flow_from_directory(batch_size=BATCH_SIZE,
                                                         directory=validation_dir,
                                                         shuffle=False,
                                                         target_size=(IMG_SHAPE, IMG_SHAPE),
                                                         class_mode='binary')

# getting MobileNet
URL = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
mobile_net = hub.KerasLayer(URL, input_shape=(IMG_SHAPE, IMG_SHAPE, 3))

mobile_net.trainable = False

model = tf.keras.models.Sequential([
    mobile_net,
    tf.keras.layers.Dense(2, activation='softmax')  # [0, 1] or [1, 0]
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

EPOCHS = 10

#THIS COMMENTED PART DOES THE ACTUAL TRAINING I'VE COMMENTED IT
#BECASUE THE MODEL HAS ALREADY BEEN TRIANED AND CAN BE FOUND IN THE CAT_DOG_MODEL DIRECTORY


# history = model.fit_generator(
#     train_data_gen,
#     steps_per_epoch=int(np.ceil(total_train / float(BATCH_SIZE))),
#     epochs=EPOCHS,
#     validation_data=val_data_gen,
#     validation_steps=int(np.ceil(total_val / float(BATCH_SIZE)))
#     )
# model.save("cat_dog_model")



#loads the trained model
model = load_model("cat_dog_model")


#FOR TESTING MAKE TWO DIRECTORTY AND POPULATE THEM WITH TEST IMAGES IN THE FORMAT OF "dog0.jpg"
for index in range(6):

    fileCounter = index
    #modify the path below for your pc
    filePath1 = "../TestImages/Dog/dog" + str(fileCounter) + ".jpg"
    filePath2 = "../TestImages/Cat/cat" + str(fileCounter) + ".jpg"
    catTest = model.predict(load_image(filePath2))
    dogTest = model.predict(load_image(filePath1))

    if dogTest[0][1] > 0.5:
        print("Prediction: Dog", "Actual: Dog")
    else:
        print("Prediction: Cat", "Actual: Dog")
    print("Dog Results: ", dogTest)

    if catTest[0][1] > 0.5:
        print("Prediction: Dog", "Actual: Cat")
    else:
        print("Prediction: Cat", "Actual: Cat")
    print("Cat Results: ", catTest)

    print("\n")









