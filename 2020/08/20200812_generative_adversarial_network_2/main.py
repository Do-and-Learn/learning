import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.python.keras import Sequential, Input
from tensorflow.python.keras.layers import Dense, LeakyReLU, Dropout
from tensorflow.python.keras.models import Model

if __name__ == '__main__':
    (X_train, _), (_, _) = mnist.load_data()
    X_train = (X_train.astype(np.float32) - 127.5) / 127.5
    X_train = X_train.reshape(60000, 784)

    randomDim = 10
    generator = Sequential(name='generator')
    generator.add(Dense(256, input_dim=randomDim))
    generator.add(LeakyReLU(0.2))
    generator.add(Dense(512))
    generator.add(LeakyReLU(0.2))
    generator.add(Dense(1024))
    generator.add(LeakyReLU(0.2))
    generator.add(Dense(784, activation='tanh'))

    discriminator = Sequential(name='discriminator')
    discriminator.add(Dense(1024, input_dim=784))
    discriminator.add(LeakyReLU(0.2))
    discriminator.add(Dropout(0.3))
    discriminator.add(Dense(512))
    discriminator.add(LeakyReLU(0.2))
    discriminator.add(Dropout(0.3))
    discriminator.add(Dense(256))
    discriminator.add(LeakyReLU(0.2))
    discriminator.add(Dropout(0.3))
    discriminator.add(Dense(1, activation='sigmoid'))

    discriminator.trainable = False
    ganInput = Input(shape=(randomDim,))
    x = generator(ganInput)
    ganOutput = discriminator(x)
    gan = Model(inputs=ganInput, outputs=ganOutput)

    discriminator.compile(loss='binary_crossentropy', optimizer='adam')
    gan.compile(loss='binary_crossentropy', optimizer='adam')

    gan.summary()
