from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.applications.inception_v3 import InceptionV3

if __name__ == '__main__':
    base_model = InceptionV3(weights='imagenet', include_top=False)

    x = base_model.output
    x = layers.Dense(1024, activation='relu')(x)
    predictions = layers.Dense(200, activation='softmax')(x)
    model = models.Model(inputs=base_model.input, outputs=predictions)

    for layer in base_model.layers:
        layer.trainable = False

    model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

    # model.fit_generator(...)

    for layer in model.layers[:172]:
        layer.trainable = False
    for layer in model.layers[172:]:
        layer.trainable = True

    model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), loss='categorical_crossentropy')

    # model.fit_generator(...)
