import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('../20201026_show_one_image/gaming.png')
    img = cv2.cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    threshold = 100
    canny_output = cv2.Canny(img, threshold, threshold * 2)
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 5)
    plt.imshow(img)
    plt.show()
