import glob
import os

import cv2
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
        gray = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)

        ax = fig.add_subplot(rows, columns, CHANNELS * i + 1)
        ax.title.set_text(name)
        ax.axis('off')
        plt.imshow(image_arr)

        meanimg = cv2.blur(image_arr, (3, 3))
        ax = fig.add_subplot(rows, columns, CHANNELS * i + 2)
        ax.title.set_text('blur')
        ax.axis('off')
        plt.imshow(meanimg)

        medianimg = cv2.medianBlur(image_arr, 3)
        ax = fig.add_subplot(rows, columns, CHANNELS * i + 3)
        ax.title.set_text('median')
        ax.axis('off')
        plt.imshow(medianimg)

        gaussianimg = cv2.GaussianBlur(image_arr, (3, 3), 0)
        ax = fig.add_subplot(rows, columns, CHANNELS * i + 4)
        ax.title.set_text('gaussian')
        ax.axis('off')
        plt.imshow(gaussianimg)

    plt.tight_layout()
    plt.savefig('img.png')
    plt.show()
