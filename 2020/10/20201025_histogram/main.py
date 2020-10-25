import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('../20201023_sobel_edge_detector_(evaluate)/img.jpg')

    color = ('blue', 'green', 'red')
    for i, histcolor in enumerate(color):
        carhistogram = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(carhistogram, color=histcolor)
        plt.xlim([0, 256])
    plt.savefig('plt.jpg')
    plt.show()
