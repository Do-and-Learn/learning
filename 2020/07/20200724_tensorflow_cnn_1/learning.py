import tensorflow as tf
from tensorflow.keras import layers, models, datasets


def build(input_shape, classes):
    model = models.Sequential()

    model.add(layers.Convolution2D(20, (5, 5), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(layers.Convolution2D(50, (5, 5), activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(layers.Flatten())
    model.add(layers.Dense(500, activation='relu'))
    model.add(layers.Dense(classes, activation='softmax'))

    return model


if __name__ == '__main__':
    EPOCHS = 5
    BATCH_SIZE = 128
    VERBOSE = 1
    OPTIMIZER = tf.keras.optimizers.Adam()
    VALIDATION_SPLIT = 0.2

    IMG_ROWS, IMG_COLS = 28, 28
    INPUT_SHAPE = (IMG_ROWS, IMG_COLS, 1)
    NB_classes = 10

    (train_data, train_labels), (evl_data, evl_labels) = datasets.mnist.load_data()

    train_data = train_data.reshape((60000, 28, 28, 1)).astype('float32')
    evl_data = evl_data.reshape((10000, 28, 28, 1)).astype('float32')

    train_data, evl_data = train_data / 255, evl_data / 255

    train_labels = tf.keras.utils.to_categorical(train_labels, NB_classes)
    evl_labels = tf.keras.utils.to_categorical(evl_labels, NB_classes)

    model = build(input_shape=INPUT_SHAPE, classes=NB_classes)
    model.compile(loss='categorical_crossentropy', optimizer=OPTIMIZER, metrics=['accuracy'])
    model.summary()

    callbacks = [
        tf.keras.callbacks.TensorBoard(log_dir='./logs')
    ]

    history = model.fit(train_data, train_labels,
                        batch_size=BATCH_SIZE, epochs=EPOCHS,
                        verbose=VERBOSE, validation_split=VALIDATION_SPLIT,
                        callbacks=callbacks)

    score = model.evaluate(train_data, train_labels, verbose=VERBOSE)
    print(f'Test score {score[0]}\nTest accuracy{score[1]}')
