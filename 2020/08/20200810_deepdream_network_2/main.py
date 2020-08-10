import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from IPython.display import clear_output


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


def deprocess(img):
    img = img.copy()
    img /= 2.
    img += 0.5
    img *= 255.
    return np.clip(img, 0, 255).astype('uint8')


def forward(img):
    img_batch = tf.expand_dims(img, axis=0)
    return feat_extraction_model(img_batch)


def calc_loss(layer_activations):
    total_loss = 0
    for act in layer_activations:
        loss = tf.math.reduce_mean(act)
        loss /= np.prod(act.shape)
        total_loss += loss
    return total_loss


if __name__ == '__main__':
    url = 'https://storage.googleapis.com/applied-dl/clouds.jpg'
    img = preprocess(download(url))
    show(deprocess(img))
    plt.show()

    names = ['mixed2', 'mixed3', 'mixed4', 'mixed5']
    inception_v3 = InceptionV3()
    layers = [inception_v3.get_layer(name).output for name in names]

    feat_extraction_model = tf.keras.Model(inputs=inception_v3.input, outputs=layers)

    img = tf.Variable(img)
    steps = 400

    for step in range(steps):
        with tf.GradientTape() as tape:
            activations = forward(img)
            loss = calc_loss(activations)
            gradients = tape.gradient(loss, img)
        gradients /= gradients.numpy().std() + 1e-8
        img.assign_add(gradients)
        print("Step %d, loss %f" % (step, loss))
        if step % 50 == 0:
            clear_output()
            show(deprocess(img.numpy()))
            plt.show()

    clear_output()
    show(deprocess(img.numpy()))
    plt.show()
