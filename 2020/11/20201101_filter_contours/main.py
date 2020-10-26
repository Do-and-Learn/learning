import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('../../10/20201026_show_one_image/gaming.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    threshold = 100
    canny_output = cv2.Canny(gray, threshold, threshold * 2)
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)

        min_size = 80
        max_size = 180
        if min_size <= w <= max_size and min_size <= h <= max_size:
            cv2.circle(img, (int(x + w / 2), int(y + h / 2)), int(w / 2), (0, 255, 255), 5)
    plt.imshow(img)
    plt.show()
