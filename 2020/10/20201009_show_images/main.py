import glob

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

if __name__ == '__main__':
    all_png = list(glob.glob('../20201007_small_dataset/piglet/*.png'))

    size = len(all_png)
    columns = 5
    rows = np.ceil(size / columns)
    fig = plt.figure(figsize=(8, 8))

    print(f'size: [{size}] rows: [{rows}] columns: [{columns}]')
    for i, png in enumerate(all_png):
        image = Image.open(png)
        print(f'png: [{png}] size: [{image.height}x{image.width}]')
        fig.add_subplot(rows, columns, i + 1)
        plt.imshow(image)
    plt.show()
