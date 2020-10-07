import glob

from PIL import Image

if __name__ == '__main__':
    all_png = list(glob.glob('../20201007_small_dataset/piglet/*.png'))

    for i, png in enumerate(all_png):
        image = Image.open(png)
        print(f'png: [{png}] size: [{image.height}x{image.width}]')
