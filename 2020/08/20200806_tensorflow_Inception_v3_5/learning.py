import tensorflow as tf
import tensorflow_datasets as tfds


def format_example(image, label):
    image = tf.cast(image, tf.float32)
    image = (image / 127.5) - 1
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    return image, label


if __name__ == '__main__':
    (raw_train, raw_validation, raw_test), metadata = tfds.load('horses_or_humans', split=['train[:80%]', 'test[:10%]', 'test[:10%]'], with_info=True, as_supervised=True)
    get_label_name = metadata.features['label'].int2str

    IMG_SIZE = 160

    train = raw_train.map(format_example)
    validation = raw_validation.map(format_example)
    test = raw_test.map(format_example)

    BATCH_SIZE = 32
    SHUFFLE_BUFFER_SIZE = 2000
    train_batches = train.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
    validation_batches = validation.batch(BATCH_SIZE)
    test_batches = test.batch(BATCH_SIZE)

    IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)
    base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights='imagenet')
    base_model.trainable = False
    base_model.summary()

    for image_batch, label_batch in train_batches.take(1):
        print(image_batch.shape)
        feature_batch = base_model(image_batch)
        print(feature_batch.shape)

        global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
        feature_batch_average = global_average_layer(feature_batch)
        prediction_layer = tf.keras.layers.Dense(1)
        prediction_batch = prediction_layer(feature_batch_average)
        print(prediction_batch.shape)
        model = tf.keras.Sequential([base_model, global_average_layer, prediction_layer])

        base_learning_rate = 0.0001
        model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=base_learning_rate), loss='binary_crossentropy', metrics=['accuracy'])

        validation_steps = 4
        initial_epochs = 10
        loss0, accuracy0 = model.evaluate(validation_batches, steps=validation_steps)

        print((loss0, accuracy0))
