from tensorflow import keras as ks

if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    mnist_fashion = ks.datasets.fashion_mnist
    (training_images, training_labels), (test_images, test_labels) = mnist_fashion.load_data()

    print(training_images.shape)  # out: (60000, 28, 28)
    print(len(training_labels))  # out: 60000
    print(test_images.shape)  # out (10000, 28, 28)
    print(len(test_labels))  # out: 10000

    # pixel 值為 0 ~ 255 的整數，將其轉換為 0 ~ 1 的浮點數 (不確定此步驟的作用，可以不要轉換嗎?)
    (training_images, test_images) = training_images / 255, test_images / 255

    training_images = training_images.reshape((*training_images.shape, 1))  # reshape to 28 * 28 * 1 array
    test_images = test_images.reshape((*test_images.shape, 1))

    print(training_images.shape)  # out: (60000, 28, 28, 1)
    print(len(training_labels))  # out: 60000
    print(test_images.shape)  # out: (10000, 28, 28, 1)
    print(len(test_labels))  # out: 10000

    cnn_model = ks.models.Sequential()
    cnn_model.add(ks.layers.Conv2D(50, (3, 3), activation='relu', input_shape=training_images.shape[1:], name='Conv2D_layer'))  # layer 1: convolutional layer with ReLU
    cnn_model.add(ks.layers.MaxPooling2D((2, 2), name='Maxpooling_2D'))  # layer 2: pooling layer

    # layer 3: fully connected layer
    cnn_model.add(ks.layers.Flatten(name='Flatten'))
    cnn_model.add(ks.layers.Dense(50, activation='relu', name='Hidden_layer'))
    cnn_model.add(ks.layers.Dense(10, activation='softmax', name='Output_layer'))

    """
    out:
    Model: "sequential"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    Conv2D_layer (Conv2D)        (None, 26, 26, 50)        500       
    _________________________________________________________________
    Maxpooling_2D (MaxPooling2D) (None, 13, 13, 50)        0         
    _________________________________________________________________
    Flatten (Flatten)            (None, 8450)              0         
    _________________________________________________________________
    Hidden_layer (Dense)         (None, 50)                422550    
    _________________________________________________________________
    Output_layer (Dense)         (None, 10)                510       
    =================================================================
    Total params: 423,560
    Trainable params: 423,560
    Non-trainable params: 0
    _________________________________________________________________
    """
    cnn_model.summary()

    cnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    cnn_model.fit(training_images, training_labels, epochs=10)  # model training

    # Training evaluation
    training_loss, training_accuracy = cnn_model.evaluate(training_images, training_labels)
    print(round(float(training_accuracy), 2))

    # Test evaluation
    test_loss, test_accuracy = cnn_model.evaluate(test_images, test_labels)
    print(format(round(float(test_accuracy), 2)))
