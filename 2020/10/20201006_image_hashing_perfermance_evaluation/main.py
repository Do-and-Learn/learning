import time

import imagehash
from PIL import Image


def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str(str1), str(str2)))


if __name__ == '__main__':
    images = ['01.png', '02.png', '03.png', '04.png'] * 100
    size = len(images)

    total_times = 0
    for image in images:
        start = time.time()
        imagehash.phash(Image.open(image))
        total_times += time.time() - start
    print(f'phash {size} images: {total_times / size} seconds')  # phash 400 images: 0.049254981875419615 seconds

    print()

    total_times = 0
    for image in images:
        start = time.time()
        imagehash.dhash(Image.open(image))
        total_times += time.time() - start
    print(f'dhash {size} images: {total_times / size} seconds')  # dhash 400 images: 0.045807921290397645 seconds
