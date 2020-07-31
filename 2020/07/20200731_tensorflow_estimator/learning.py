import numpy as np
import tensorflow as tf

LABEL_DIMENSIONS = 10


def input_fn(images, labels, epochs, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((images, labels))
    SHUFFLE_SIZE = 5000
    dataset = dataset.shuffle(SHUFFLE_SIZE).repeat(epochs).batch(batch_size)
    dataset = dataset.prefetch(None)
    return dataset


if __name__ == '__main__':
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
    TRAINING_SIZE = len(train_images)
    TEST_SIZE = len(test_images)

    train_images = train_images.reshape((TRAINING_SIZE, 28, 28, 1))
    train_images = np.asarray(train_images, dtype=np.float32) / 255

    test_images = test_images.reshape((TEST_SIZE, 28, 28, 1))
    test_images = np.asarray(test_images, dtype=np.float32) / 255

    train_labels = tf.keras.utils.to_categorical(train_labels, LABEL_DIMENSIONS)
    test_labels = tf.keras.utils.to_categorical(test_labels, LABEL_DIMENSIONS)

    train_labels = train_labels.astype(np.float32)
    test_labels = test_labels.astype(np.float32)
    print(train_labels.shape)
    print(test_labels.shape)

    inputs = tf.keras.Input(shape=(28, 28, 1))
    x = tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu')(inputs)
    x = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    x = tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu')(x)
    x = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    x = tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu')(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    predictions = tf.keras.layers.Dense(LABEL_DIMENSIONS, activation='softmax')(x)
    model = tf.keras.Model(inputs=inputs, outputs=predictions)
    model.summary()

    optimizer = tf.keras.optimizers.SGD()
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    strategy = None
    # strategy = tf.distribute.MirroredStrategy()
    config = tf.estimator.RunConfig(train_distribute=strategy)
    estimator = tf.keras.estimator.model_to_estimator(model, config=config)

    BATCH_SIZE = 512
    EPOCHS = 50
    tf.get_logger().setLevel('DEBUG')
    estimator_train_result = estimator.train(input_fn=lambda: input_fn(train_images, train_labels, epochs=EPOCHS, batch_size=BATCH_SIZE))
    print(estimator_train_result)

    result = estimator.evaluate(lambda: input_fn(test_images, test_labels, epochs=1, batch_size=BATCH_SIZE))
    print(result)  # {'accuracy': 0.8424, 'loss': 0.4409616, 'global_step': 5860}
