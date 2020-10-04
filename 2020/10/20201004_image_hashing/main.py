import imagehash
from PIL import Image

if __name__ == '__main__':
    phash1 = imagehash.phash(Image.open('01.png'))  # e9cacf3192c61879
    phash2 = imagehash.phash(Image.open('02.png'))  # e9cece3192c61879
    phash3 = imagehash.phash(Image.open('03.png'))  # 94b46b69695a3696
    phash4 = imagehash.phash(Image.open('04.png'))  # 95e46a523e2f60cb
    print(f'phash 1: {phash1}')
    print(f'phash 2: {phash2}')
    print(f'phash 3: {phash3}')
    print(f'phash 4: {phash4}')

    dhash1 = imagehash.dhash(Image.open('01.png'))  # 880f334d9e160717
    dhash2 = imagehash.dhash(Image.open('02.png'))  # 880f334d9e160717
    dhash3 = imagehash.dhash(Image.open('03.png'))  # 33ccec98d4cce869
    dhash4 = imagehash.dhash(Image.open('04.png'))  # 31e8c296fcc4e869
    print(f'dhash 1: {dhash1}')
    print(f'dhash 2: {dhash2}')
    print(f'dhash 3: {dhash3}')
    print(f'dhash 4: {dhash4}')
