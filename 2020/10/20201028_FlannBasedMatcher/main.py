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

    flann = cv2.FlannBasedMatcher(dict(algorithm=0, trees=7), dict(checks=50))
    matches = flann.knnMatch(des1, des2, k=2)
    matchesMask = [[0, 0] for i in range(len(matches))]

    for i, (match1, match2) in enumerate(matches):
        if match1.distance < 1.2 * match2.distance:
            matchesMask[i] = [1, 0]

    draw_params = dict(matchColor=(255, 0, 0), singlePointColor=(0, 0, 255), matchesMask=matchesMask, flags=2)
    flann_matches = cv2.drawMatchesKnn(target, kp1, gaming, kp2, matches, None, **draw_params)

    plt.imshow(flann_matches)
    plt.show()
