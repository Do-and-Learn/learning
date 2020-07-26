import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models


# noinspection PyShadowingNames
def build(input_shape, classes):
    model = models.Sequential()

    model.add(layers.Convolution2D(32, (3, 3), activation='relu', padding='same', input_shape=input_shape))
    model.add(layers.BatchNormalization())
    model.add(layers.Convolution2D(32, (3, 3), activation='relu', padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.2))

    model.add(layers.Convolution2D(64, (3, 3), activation='relu', padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Convolution2D(64, (3, 3), activation='relu', padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.3))

    model.add(layers.Convolution2D(128, (3, 3), activation='relu', padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Convolution2D(128, (3, 3), activation='relu', padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.4))

    model.add(layers.Flatten())
    model.add(layers.Dense(classes, activation='softmax'))

    return model


if __name__ == '__main__':
    IMG_CHANNELS = 3
    IMG_ROWS = 32
    IMG_COLS = 32

    BATCH_SIZE = 64
    EPOCHS = 50
    CLASSES = 10
    VERBOSE = 1
    VALIDATION_SPLIT = 0.2
    OPTIM = tf.keras.optimizers.RMSprop()

    (train_data, train_labels), (test_data, test_labels) = datasets.cifar10.load_data()
    mean = np.mean(train_data, axis=(0, 1, 2, 3))
    std = np.std(train_data, axis=(0, 1, 2, 3))
    train_data = (train_data - mean) / (std + 1e-7)
    test_data = (test_data - mean) / (std + 1e-7)

    train_labels = tf.keras.utils.to_categorical(train_labels, CLASSES)
    test_labels = tf.keras.utils.to_categorical(test_labels, CLASSES)

    callbacks = [
        tf.keras.callbacks.TensorBoard(log_dir='./logs')
    ]

    model = build((IMG_ROWS, IMG_ROWS, IMG_CHANNELS), CLASSES)
    model.compile(loss='categorical_crossentropy', optimizer=OPTIM, metrics=['accuracy'])
    model.fit(train_data, train_labels, batch_size=BATCH_SIZE,
              epochs=EPOCHS, validation_split=VALIDATION_SPLIT,
              verbose=VERBOSE, callbacks=callbacks)

    score = model.evaluate(test_data, test_labels, batch_size=BATCH_SIZE, verbose=VERBOSE)

    print(f'Test score {score[0]}\nTest accuracy {score[1]}')
