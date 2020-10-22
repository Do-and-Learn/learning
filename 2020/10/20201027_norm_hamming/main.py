import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    gaming = cv2.imread('../20201026_show_one_image/gaming.png')
    gaming = cv2.cvtColor(gaming, cv2.COLOR_BGR2RGB)

    target = cv2.imread('../20201026_show_one_image/005.png')
    target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(target, None)
    kp2, des2 = orb.detectAndCompute(gaming, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = sorted(bf.match(des1, des2), key=lambda x: x.distance)

    target_matches = cv2.drawMatches(target, kp1, gaming, kp2, matches[:50], None, flags=2)
    plt.imshow(target_matches)
    plt.savefig('norm_hamming.png')
    plt.show()
