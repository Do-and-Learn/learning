import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    gaming = cv2.imread('../20201026_show_one_image/gaming.png')
    gaming = cv2.cvtColor(gaming, cv2.COLOR_BGR2RGB)

    target = cv2.imread('../20201026_show_one_image/005.png')
    target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)

    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(target, None)
    kp2, des2 = sift.detectAndCompute(gaming, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for match1, match2 in matches:
        if match1.distance < 1.2 * match2.distance:
            good.append([match1])
    draw_params = dict(matchColor=(0, 0, 255), singlePointColor=(0, 0, 255))
    sift_matches = cv2.drawMatchesKnn(target, kp1, gaming, kp2, good, None, **draw_params)
    plt.imshow(sift_matches)
    plt.show()
