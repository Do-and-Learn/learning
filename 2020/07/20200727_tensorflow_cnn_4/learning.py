import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json

if __name__ == '__main__':
    model_architecture = 'model.json'
    model_weights = 'model.h5'
    model = model_from_json(open(model_architecture).read())
    model.load_weights(model_weights)

    img_names = ['cat.jpg', 'dog.jpg']

    imgs = [tf.image.resize(tf.image.decode_jpeg(tf.io.read_file(img_name), channels=3), [32, 32]) for img_name in img_names]
    imgs = [np.transpose(img, (2, 0, 1)).reshape((32, 32, 3)).astype('float32') for img in imgs]
    imgs = np.array(imgs) / 255

    optim = tf.keras.optimizers.SGD()
    model.compile(loss='categorical_crossentropy', optimizer=optim, metrics=['accuracy'])

    predictions = np.argmax(model.predict(imgs), axis=-1)
    print(predictions)
