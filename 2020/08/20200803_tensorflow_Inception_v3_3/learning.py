import tensorflow_datasets as tfds
import matplotlib.pyplot as plt


def show_images(dataset):
    get_label_name = metadata.features['label'].int2str
    for image, label in dataset.take(10):
        plt.figure()
        plt.imshow(image)
        plt.title(get_label_name(label))
    plt.show()


if __name__ == '__main__':
    (raw_train, raw_validation, raw_test), metadata = tfds.load(
        'horses_or_humans',
        split=['train[:80%]', 'test[:10%]', 'test[:10%]'],
        with_info=True,
        as_supervised=True)

    show_images(raw_train)
