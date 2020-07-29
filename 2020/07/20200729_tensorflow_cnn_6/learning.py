import json

import cv2
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16


def load_img(img_path):
    im = cv2.resize(cv2.imread(img_path), (224, 224))
    im = np.expand_dims(im, axis=0)
    return im


if __name__ == '__main__':
    with open('labels.json') as f:
        labels = json.load(f)
    model = VGG16(weights='imagenet', include_top=True)
    model.compile(optimizer='sgd', loss='categorical_crossentropy')

    out = model.predict(load_img('cat.jpg'))
    index = np.argmax(out)
    print(f'{index}: {labels[index]}')
    plt.plot(out.ravel())
    plt.show()

    out = model.predict(load_img('dog.jpg'))
    index = np.argmax(out)
    print(f'{index}: {labels[index]}')
    plt.plot(out.ravel())
    plt.show()

    out = model.predict(load_img('cat-standing.jpg'))
    index = np.argmax(out)
    print(f'{index}: {labels[index]}')
    plt.plot(out.ravel())
    plt.show()
