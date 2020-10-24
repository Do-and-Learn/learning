import cv2

if __name__ == '__main__':
    img = cv2.imread('../20201026_show_one_image/gaming.png')
    threshold = 100
    canny_output = cv2.Canny(img, threshold, threshold * 2)

    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f'contours: {len(contours)}')  # contours: 2186
