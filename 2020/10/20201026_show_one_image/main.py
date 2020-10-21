import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    gaming = cv2.imread('gaming.png')
    gaming = cv2.cvtColor(gaming, cv2.COLOR_BGR2RGB)
    plt.imshow(gaming)
    plt.show()
