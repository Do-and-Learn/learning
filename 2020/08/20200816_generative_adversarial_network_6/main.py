import os

import matplotlib.pylab as plt
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.optimizers import Adam
from tensorflow.python.keras import Sequential, Input
from tensorflow.python.keras.layers import Dense, LeakyReLU, Dropout
from tensorflow.python.keras.models import Model


def train(epochs=1, batch_size=128):
    batch_count = int(x_train.shape[0] / batch_size)
    print(f'Epochs: {epochs}')
    print(f'Batch size: {batch_size}')
    print(f'Batches per epoch: {batch_count}')

    for e in range(1, epochs + 1):
        print(f'Epoch {e}'.center(50, '-'))
        generated_images = None
        for i in range(batch_count):
            # Get a random set of input noise and images
            noise = np.random.normal(0, 1, size=[batch_size, random_dim])

            real_images = x_train[np.random.randint(0, x_train.shape[0], size=batch_size)]

            # Generate fake MNIST images
            generated_images = generator.predict(noise)

            images = np.concatenate([real_images, generated_images])

            labels = np.zeros(2 * batch_size)

            labels[:batch_size] = 1

            discriminator.trainable = True
            dloss = discriminator.train_on_batch(images, labels)

            labels = np.ones(batch_size)
            discriminator.trainable = False
            gloss = gan.train_on_batch(noise, labels)

        if e == 1 or e % 20 == 0:
            save_generated_images(generated_images, e)


def save_generated_images(images, epoch, dim=(10, 10), figsize=(10, 10)):
    images = images.reshape(images.shape[0], 28, 28)
    os.makedirs('images', exist_ok=True)
    plt.figure(figsize=figsize)
    for i in range(min(images.shape[0], 100)):
        plt.subplot(dim[0], dim[1], i + 1)
        plt.imshow(images[i], interpolation='nearest', cmap='gray_r')
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('images/gan_generated_image_epoch_%d.png' % epoch)


if __name__ == '__main__':
    (x_train, _), (_, _) = mnist.load_data()
    x_train = (x_train.astype(np.float32) - 127.5) / 127.5
    x_train = x_train.reshape(60000, 784)

    random_dim = 10
    generator = Sequential(name='generator')
    generator.add(Dense(256, input_dim=random_dim))
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
    discriminator.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.0002, beta_1=0.5))

    discriminator.trainable = False
    ganInput = Input(shape=(random_dim,))
    x = generator(ganInput)
    ganOutput = discriminator(x)
    gan = Model(inputs=ganInput, outputs=ganOutput)
    gan.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.0002, beta_1=0.5))

    gan.summary()
    train(epochs=200)
