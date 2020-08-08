import PIL.Image as Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

if __name__ == '__main__':
    classifier_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
    IMAGE_SHAPE = (224, 224)
    classifier = tf.keras.Sequential([hub.KerasLayer(classifier_url, input_shape=IMAGE_SHAPE + (3,))])

    grace_hopper = tf.keras.utils.get_file('image.jpg', 'https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg')
    grace_hopper = Image.open(grace_hopper).resize(IMAGE_SHAPE)
    grace_hopper = np.array(grace_hopper) / 255.0
    result = classifier.predict(grace_hopper[np.newaxis, ...])
    predicted_class = np.argmax(result[0], axis=-1)

    with open('ImageNetLabels.txt') as f:
        labels = f.read().split('\n')

    print(f'{predicted_class}: {labels[int(predicted_class)]}')
