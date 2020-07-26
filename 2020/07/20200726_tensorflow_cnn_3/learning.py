import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# noinspection PyShadowingNames
def build_model(input_shape, classes):
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

    EPOCHS = 20
    CLASSES = 10
    VERBOSE = 1
    VALIDATION_SPLIT = 0.2
    OPTIM = tf.keras.optimizers.RMSprop()

    (train_data, train_labels), (test_data, test_labels) = datasets.cifar10.load_data()
    train_data = train_data.astype('float32')
    test_data = test_data.astype('float32')

    mean = np.mean(train_data, axis=(0, 1, 2, 3))
    std = np.std(train_data, axis=(0, 1, 2, 3))
    train_data = (train_data - mean) / (std + 1e-7)
    test_data = (test_data - mean) / (std + 1e-7)

    datagen = ImageDataGenerator(
        rotation_range=30,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True
    )
    datagen.fit(train_data)

    train_labels = tf.keras.utils.to_categorical(train_labels, CLASSES)
    test_labels = tf.keras.utils.to_categorical(test_labels, CLASSES)

    callbacks = [
        tf.keras.callbacks.TensorBoard(log_dir='./logs')
    ]

    model = build_model(train_data.shape[1:], CLASSES)
    model.compile(loss='categorical_crossentropy', optimizer=OPTIM, metrics=['accuracy'])
    model.fit_generator(datagen.flow(train_data, train_labels, batch_size=64),
                        epochs=EPOCHS, verbose=VERBOSE, callbacks=callbacks,
                        validation_data=(test_data, test_labels))

    model_json = model.to_json()
    with open('model.json', 'w') as json_file:
        json_file.write(model_json)
    model.save_weights('model.h5')

    score = model.evaluate(test_data, test_labels, batch_size=128, verbose=VERBOSE)

    print(f'Test score {score[0]}\nTest accuracy {score[1]}')
