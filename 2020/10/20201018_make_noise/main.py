import glob
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage.util import random_noise

if __name__ == '__main__':
    all_png = list(glob.glob('../20201007_small_dataset/piglet/*.png'))

    CHANNELS = 2
    size = len(all_png) * CHANNELS
    columns = 3 * CHANNELS
    rows = np.ceil(size / columns)
    fig = plt.figure(figsize=(8, 8))

    print(f'size: [{size}] rows: [{rows}] columns: [{columns}]')
    for i, png in enumerate(all_png):
        name = os.path.basename(png)
        image = Image.open(png)
        print(f'png: [{name}] size: [{image.height}x{image.width}]')

        image_arr = np.asarray(image)
        gray = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)

        ax = fig.add_subplot(rows, columns, CHANNELS * i + 1)
        ax.title.set_text(name)
        ax.axis('off')
        plt.imshow(image_arr)

        imgnoise = random_noise(image_arr, mode='s&p', amount=0.3)
        ax = fig.add_subplot(rows, columns, CHANNELS * i + 2)
        ax.axis('off')
        plt.imshow(imgnoise)

    plt.tight_layout()
    plt.savefig('img.png')
    plt.show()
