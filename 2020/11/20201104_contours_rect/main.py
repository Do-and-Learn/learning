import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('../../10/20201026_show_one_image/gaming.png')
    img = cv2.cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    threshold = 100
    canny_output = cv2.Canny(img, threshold, threshold * 2)
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        min_size = 100
        max_size = 150
        if min_size <= w <= max_size and min_size <= h <= max_size:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    plt.imshow(img)
    plt.show()
