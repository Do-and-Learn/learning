import time

import cv2

if __name__ == '__main__':
    img = cv2.imread('../20201023_sobel_edge_detector_(evaluate)/img.jpg')
    start = time.time()
    try:
        canny = cv2.Canny(img, threshold1=100, threshold2=200)
        cv2.imwrite('canny.jpg', canny)
    finally:
        print(f'{time.time() - start:.2f} s')  # 0.36 s
