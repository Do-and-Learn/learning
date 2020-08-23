import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds


def normalize(input_image, label):
    input_image = tf.cast(input_image, tf.float32)
    input_image = (input_image / 127.5) - 1
    return input_image


if __name__ == '__main__':
    # https://www.tensorflow.org/datasets/catalog/cycle_gan#cycle_gansummer2winter_yosemite
    # https://www.tensorflow.org/tutorials/load_data/images
    data_dir = tf.keras.utils.get_file(origin='https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/summer2winter_yosemite.zip', fname='summer2winter_yosemite.zip', extract=True)

    dataset = tf.keras.preprocessing.image_dataset_from_directory(f'{os.path.dirname(data_dir)}/summer2winter_yosemite')
    class_names = dataset.class_names
    dataset = dataset.unbatch()
    train_A = dataset.filter(lambda _, label: label == class_names.index('trainA'))
    train_B = dataset.filter(lambda _, label: label == class_names.index('trainB'))
    test_A = dataset.filter(lambda _, label: label == class_names.index('testA'))
    test_B = dataset.filter(lambda _, label: label == class_names.index('testB'))

    BUFFER_SIZE = 1000
    BATCH_SIZE = 1
    IMG_WIDTH = 256
    IMG_HEIGHT = 256
    EPOCHS = 50
    AUTOTUNE = tf.data.experimental.AUTOTUNE

    train_A = train_A.map(normalize, num_parallel_calls=AUTOTUNE).cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
    train_B = train_B.map(normalize, num_parallel_calls=AUTOTUNE).cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
    test_A = test_A.map(normalize, num_parallel_calls=AUTOTUNE).cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
    test_B = test_B.map(normalize, num_parallel_calls=AUTOTUNE).cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

    inpA = next(iter(train_A))
    inpB = next(iter(train_B))
    plt.subplot(121)
    plt.title('Train Set A (summer)')
    plt.imshow(inpA[0] * 0.5 + 0.5)
    plt.subplot(122)
    plt.title('Train Set B (winter)')
    plt.imshow(inpB[0] * 0.5 + 0.5)
    plt.show()
