import cv2
from skimage.feature import local_binary_pattern


def show_image(title, image, resize_rate=0.5):
    image = cv2.resize(image, dsize=(int(img.shape[1] * resize_rate), int(img.shape[0] * resize_rate)))
    cv2.imshow(title, image)
    cv2.waitKey(0)


if __name__ == '__main__':
    radius = 7
    n_points = int((8 * radius + 16) / 3)
    img = cv2.imread('../../10/20201026_show_one_image/gaming.png')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    lbp = local_binary_pattern(img, n_points, radius)
    show_image('lbp_image', lbp)
