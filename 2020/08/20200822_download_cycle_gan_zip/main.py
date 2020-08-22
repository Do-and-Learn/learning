import tensorflow_datasets as tfds
import tensorflow as tf

if __name__ == '__main__':
    # https://www.tensorflow.org/datasets/catalog/cycle_gan#cycle_gansummer2winter_yosemite
    data_dir = tf.keras.utils.get_file(origin='https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/summer2winter_yosemite.zip', fname='summer2winter_yosemite.zip')
    print(data_dir)
