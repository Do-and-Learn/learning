import os

import cv2
import numpy as np

if __name__ == '__main__':
    JPG_QUALITY = 70
    os.makedirs('out', exist_ok=True)
    img = cv2.imread('img.jpg')
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imwrite('out/rgb_sobel_x.jpg', sobel_x, [cv2.IMWRITE_JPEG_QUALITY, JPG_QUALITY])
    cv2.imwrite('out/rgb_sobel_y.jpg', sobel_y, [cv2.IMWRITE_JPEG_QUALITY, JPG_QUALITY])

    # mag, direction = cv2.cartToPolar(sobel_x, sobel_y, angleInDegrees=True)
    sobel_g = np.hypot(sobel_x, sobel_y)
    cv2.imwrite('out/rgb_sobel_g.jpg', sobel_g, [cv2.IMWRITE_JPEG_QUALITY, JPG_QUALITY])

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imwrite('out/gray_sobel_x.jpg', sobel_x, [cv2.IMWRITE_JPEG_QUALITY, JPG_QUALITY])
    cv2.imwrite('out/gray_sobel_y.jpg', sobel_y, [cv2.IMWRITE_JPEG_QUALITY, JPG_QUALITY])

    sobel_g = np.hypot(sobel_x, sobel_y)
    cv2.imwrite('out/gray_sobel_g.jpg', sobel_g, [cv2.IMWRITE_JPEG_QUALITY, JPG_QUALITY])
