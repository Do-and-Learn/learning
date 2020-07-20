import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    np.random.seed(0)
    area = 2.5 * np.random.randn(100) + 25
    price = 25 * area + 5 + np.random.randint(20, 50, size=len(area))

    data = np.array([area, price])
    data = pd.DataFrame(data=data.T, columns=['area', 'price'])

    w = sum(price * (area - np.mean(area))) / sum((area - np.mean(area)) ** 2)
    b = np.mean(price) - w * np.mean(area)

    y_pred = w * area + b
    plt.plot(area, y_pred, color='red', label="Predicted Price")
    plt.scatter(data['area'], data['price'], label="Training Data")
    plt.xlabel("Area")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
