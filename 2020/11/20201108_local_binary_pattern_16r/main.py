import cv2
import matplotlib.pyplot as plt
from skimage.feature import local_binary_pattern

if __name__ == '__main__':
    img = cv2.imread('../../10/20201026_show_one_image/005.png')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    fig = plt.figure(figsize=(8, 8))
    for radius in range(16):
        n_points = (8 * (radius + 1))
        lbp = local_binary_pattern(img, n_points, radius + 1)
        ax = fig.add_subplot(4, 4, radius + 1)
        ax.axis('off')
        ax.title.set_text(f'R={radius+1}, P={n_points}')
        plt.imshow(lbp, cmap='gray')
    plt.savefig('out.png')
    plt.show()
