import tensorflow as tf

if __name__ == '__main__':
    mnist = tf.keras.datasets.mnist

    # load_data() will download MNIST data set.
    (x_train, y_train), (x_test, y_test) = mnist.load_data()  # TODO how to interpret structure of x, y train and x, y test
    x_train, x_test = x_train / 255.0, x_test / 255.0  # TODO why x data need to divide 255

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)
    print(model.evaluate(x_test, y_test))
