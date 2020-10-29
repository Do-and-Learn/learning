import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('../../10/20201026_show_one_image/gaming.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    threshold = 100
    canny_output = cv2.Canny(gray, threshold, threshold * 2)
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    thickness = 10
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)

        min_size = 80
        max_size = 180
        if min_size <= w <= max_size and min_size <= h <= max_size:
            text_loc = (x + int(w / 2) - 10, y + int(h / 2) + 10)
            roi = img[y: y + h, x: x + w]
            roi_mean_color = cv2.mean(roi)
            if roi_mean_color[0] > roi_mean_color[1] > roi_mean_color[2]:
                color = (0, 255, 0)
                cv2.putText(img, '1', text_loc, font, 2, color, thickness, cv2.LINE_AA)
                cv2.circle(img, (x + int(w / 2), y + int(h / 2)), int(w / 2), color, 5)
            elif roi_mean_color[1] > roi_mean_color[2] > roi_mean_color[0]:
                color = (135, 215, 221)
                cv2.putText(img, '2', text_loc, font, 2, color, thickness, cv2.LINE_AA)
                cv2.circle(img, (x + int(w / 2), y + int(h / 2)), int(w / 2), color, 5)
            elif roi_mean_color[0] > roi_mean_color[2] > roi_mean_color[1]:
                color = (255, 73, 255)
                cv2.putText(img, '3', text_loc, font, 2, color, thickness, cv2.LINE_AA)
                cv2.circle(img, (x + int(w / 2), y + int(h / 2)), int(w / 2), color, 5)
            else:
                color = (0, 255, 255)
                cv2.putText(img, '4', text_loc, font, 2, color, thickness, cv2.LINE_AA)
                cv2.circle(img, (int(x + w / 2), int(y + h / 2)), int(w / 2), color, 5)
    plt.imshow(img)
    plt.show()
