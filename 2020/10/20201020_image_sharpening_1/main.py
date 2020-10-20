import numpy as np

if __name__ == '__main__':
    m1 = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])
    m2 = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])
    print(m1 * m2)
