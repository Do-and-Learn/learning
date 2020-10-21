import glob
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

if __name__ == '__main__':
    all_png = list(glob.glob('../20201007_small_dataset/piglet/*.png'))

    CHANNELS = 2
    size = len(all_png) * CHANNELS
    columns = 3 * CHANNELS
    rows = int(np.ceil(size / columns))
    fig = plt.figure(figsize=(8, 8))

    print(f'size: [{size}] rows: [{rows}] columns: [{columns}]')
    for i, png in enumerate(all_png):
        name = os.path.basename(png)
        image = Image.open(png)

        image_arr = np.asarray(image)
        gray = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)

        ax = fig.add_subplot(rows, columns, CHANNELS * i + 1)
        ax.title.set_text(name)
        ax.axis('off')
        plt.imshow(gray, cmap='gray')

        lap_image = cv2.Laplacian(gray, -1)
        ax = fig.add_subplot(rows, columns, CHANNELS * i + 2)
        ax.axis('off')
        plt.imshow(lap_image, cmap='gray_r')

    plt.tight_layout()
    plt.savefig('img.png')
    plt.show()
