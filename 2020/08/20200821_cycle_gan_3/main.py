import tensorflow as tf

if __name__ == '__main__':
    # https://www.tensorflow.org/datasets/catalog/cycle_gan#cycle_gansummer2winter_yosemite
    dataset = tf.keras.preprocessing.image_dataset_from_directory('summer2winter_yosemite')

    for images, labels in dataset:
        pass
