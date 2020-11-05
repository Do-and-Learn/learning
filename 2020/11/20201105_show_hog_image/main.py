import cv2
from skimage.feature import hog


def show_image(title, image, resize_rate=0.5):
    image = cv2.resize(image, dsize=(int(img.shape[1] * resize_rate), int(img.shape[0] * resize_rate)))
    cv2.imshow(title, image)
    cv2.waitKey(0)


if __name__ == '__main__':
    img = cv2.imread('../../10/20201026_show_one_image/gaming.png')
    obj, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
    show_image('hog_image', hog_image)
