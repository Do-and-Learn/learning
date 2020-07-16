import tensorflow as tf
from tensorflow import keras

if __name__ == '__main__':
    tf.random.set_seed(0)  # round 3: added
    EPOCHS = 50  # round 5: 10 -> 50
    BATCH_SIZE = 128
    VERBOSE = 1
    NB_CLASSES = 10
    N_HIDDEN = 128
    VALIDATION_SPLIT = 0.2
    DROPOUT = 0.3  # round 3: added

    mnist = keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255, x_test / 255

    RESHAPED = 784

    # print(x_train.shape)
    x_train = x_train.reshape(60000, RESHAPED)
    x_test = x_test.reshape(10000, RESHAPED)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    y_train = tf.keras.utils.to_categorical(y_train, NB_CLASSES)
    y_test = tf.keras.utils.to_categorical(y_test, NB_CLASSES)

    model = tf.keras.models.Sequential()
    model.add(keras.layers.Dense(N_HIDDEN, input_shape=(RESHAPED,), name='dense_layer', activation='relu'))  # round 2: added
    model.add(keras.layers.Dropout(DROPOUT))  # round 3: added
    model.add(keras.layers.Dense(N_HIDDEN, name='dense_layer_2', activation='relu'))  # round 2: added
    model.add(keras.layers.Dropout(DROPOUT))  # round 3: added
    model.add(keras.layers.Dense(NB_CLASSES, input_shape=(RESHAPED,), name='dense_layer_3', activation='softmax'))  # round 2: rename "dense_layer" -> "dense_layer_3"

    model.summary()  # round 2: added

    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])  # round 5: RMSProp -> Adam
    model.fit(x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=VERBOSE, validation_split=VALIDATION_SPLIT)
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print('Test accuracy:', test_acc)
