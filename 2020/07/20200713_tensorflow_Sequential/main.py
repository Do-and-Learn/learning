import tensorflow as tf
from tensorflow import keras

if __name__ == '__main__':
    NB_CLASSES = 10  # 單層，10 個人工神經元
    RESHAPED = 784  # 輸入的變數量 (特徵值)
    model = tf.keras.models.Sequential()

    # Dense: 該層的每一個神經元連接上層的所有神經元，並連接至下層的所有神經元
    # kernel_initializer: 神經元的權重。
    #   - random_uniform: 隨機值 -0.05 ~ 0.05
    #   - random_normal: 隨機值，基於平均值為 0 的 高斯分布(Gaussian distribution，又稱 常態分布)，標準差 0.05
    #   - zero: 0
    model.add(keras.layers.Dense(NB_CLASSES, input_shape=(RESHAPED,), kernel_initializer='zeros', name='dense_layer', activation='softmax'))
