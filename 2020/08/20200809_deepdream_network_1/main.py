import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image


def download(url):
    name = url.split("/")[-1]
    image_path = tf.keras.utils.get_file(name, origin=url)
    img = image.load_img(image_path)
    return image.img_to_array(img)


def preprocess(img):
    return (img / 127.5) - 1


def show(img):
    plt.figure(figsize=(12, 12))
    plt.grid(False)
    plt.axis('off')
    plt.imshow(img)
    # plt.show()


def deprocess(img):
    img = img.copy()
    img /= 2.
    img += 0.5
    img *= 255.
    return np.clip(img, 0, 255).astype('uint8')


if __name__ == '__main__':
    url = 'https://storage.googleapis.com/applied-dl/clouds.jpg'
    img = preprocess(download(url))
    show(deprocess(img))
    plt.show()
