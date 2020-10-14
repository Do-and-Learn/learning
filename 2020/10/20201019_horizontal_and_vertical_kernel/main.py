import glob
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

if __name__ == '__main__':
    all_png = list(glob.glob('../20201007_small_dataset/piglet/*.png'))

    CHANNELS = 3
    size = len(all_png) * CHANNELS
    columns = 3 * CHANNELS
    rows = np.ceil(size / columns)
    fig = plt.figure(figsize=(8, 8))

    horizontal_kernel = np.array([[-1, -1, -1],
                                  [2, 2, 2],
                                  [-1, -1, -1]])

    vertical_kernel = np.array([[-1, 2, -1],
                                [-1, 2, -1],
                                [-1, 2, -1]])

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

        himg = cv2.filter2D(gray, -1, horizontal_kernel)
        ax = fig.add_subplot(rows, columns, CHANNELS * i + 2)
        ax.axis('off')
        plt.imshow(himg, cmap='gray_r')

        vimg = cv2.filter2D(gray, -1, vertical_kernel)
        ax = fig.add_subplot(rows, columns, CHANNELS * i + 3)
        ax.axis('off')
        plt.imshow(vimg, cmap='gray_r')

    plt.tight_layout()
    plt.savefig('img.png')
    plt.show()
