import glob
import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

if __name__ == '__main__':
    all_png = list(glob.glob('../20201007_small_dataset/piglet/*.png'))

    CHANNELS = 4
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

        ax = fig.add_subplot(rows, columns, CHANNELS * i + 1)
        ax.title.set_text(name)
        ax.axis('off')
        plt.imshow(image_arr)

        ax = fig.add_subplot(rows, columns, CHANNELS * i + 2)
        ax.axis('off')
        plt.imshow(image_arr[:, :, 0], cmap='gray')

        ax = fig.add_subplot(rows, columns, CHANNELS * i + 3)
        ax.axis('off')
        plt.imshow(image_arr[:, :, 1], cmap='gray')

        ax = fig.add_subplot(rows, columns, CHANNELS * i + 4)
        ax.axis('off')
        plt.imshow(image_arr[:, :, 2], cmap='gray')

    plt.show()
