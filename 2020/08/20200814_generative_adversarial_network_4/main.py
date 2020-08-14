import os

import matplotlib.pylab as plt
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.python.keras import Sequential, Input
from tensorflow.python.keras.layers import Dense, LeakyReLU, Dropout
from tensorflow.python.keras.models import Model


# def save_generated_images(epoch, examples=100, dim=(10, 10), fig_size=(10, 10)):
#     noise = np.random.normal(0, 1, size=[examples, random_dim])
#     generated_images = generator.predict(noise)
#     generated_images = generated_images.reshape(examples, 28, 28)
#     plt.figure(figsize=fig_size)
#     os.makedirs('images', exist_ok=True)
#     for i in range(generated_images.shape[0]):
#         plt.subplot(dim[0], dim[1], i + 1)
#         plt.imshow(generated_images[i], interpolation='nearest', cmap='gray_r')
#         plt.axis('off')
#         plt.tight_layout()
#         plt.savefig('images/gan_generated_image_epoch_%d.png' % epoch)

def train(epochs=1, batch_size=128):
    batch_count = int(X_train.shape[0] / batch_size)
    print(f'Epochs: {epochs}')
    print(f'Batch size: {batch_size}')
    print(f'Batches per epoch: {batch_count}')
    os.makedirs('images', exist_ok=True)
    for e in range(1, epochs + 1):
        print(f'Epoch {e}'.center(50, '-'))
        for i in range(batch_count):
            # Get a random set of input noise and images
            noise = np.random.normal(0, 1, size=[batch_size, random_dim])

            # Generate fake MNIST images
            generated_images = generator.predict(noise)
            for j, image in enumerate(generated_images):
                save_image(image, f'images/epoch{e}-{i}({j}).png')


def save_image(generated_images, path):
    image = generated_images.reshape(28, 28)
    plt.imshow(image, interpolation='nearest', cmap='gray_r')
    plt.savefig(path)


if __name__ == '__main__':
    (X_train, _), (_, _) = mnist.load_data()
    X_train = (X_train.astype(np.float32) - 127.5) / 127.5
    X_train = X_train.reshape(60000, 784)

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

    discriminator.trainable = False
    ganInput = Input(shape=(random_dim,))
    x = generator(ganInput)
    ganOutput = discriminator(x)
    gan = Model(inputs=ganInput, outputs=ganOutput)

    discriminator.compile(loss='binary_crossentropy', optimizer='adam')
    gan.compile(loss='binary_crossentropy', optimizer='adam')

    gan.summary()
    train(1)
