import pandas as pd
import tensorflow as tf
from tensorflow import feature_column as fc
from tensorflow.keras.datasets import boston_housing


def estimator_input_fn(df_data, df_label, epochs=10, shuffle=True, batch_size=32):
    def input_function():
        ds = tf.data.Dataset.from_tensor_slices((dict(df_data), df_label))
        if shuffle:
            ds = ds.shuffle(100, seed=0)
        ds = ds.batch(batch_size).repeat(epochs)
        return ds

    return input_function


if __name__ == '__main__':
    ((x_train, y_train), (x_test, y_test)) = boston_housing.load_data()
    features = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

    x_train_df = pd.DataFrame(x_train, columns=features)
    x_test_df = pd.DataFrame(x_test, columns=features)
    y_train_df = pd.DataFrame(y_train, columns=['MEDV'])
    y_test_df = pd.DataFrame(y_test, columns=['MEDV'])
    x_train_df.head()

    feature_columns = [fc.numeric_column(feature_name, dtype=tf.float32) for feature_name in features]

    train_input_fn = estimator_input_fn(x_train_df, y_train_df)
    val_input_fn = estimator_input_fn(x_test_df, y_test_df, epochs=1, shuffle=False)

    linear_est = tf.estimator.LinearRegressor(feature_columns=feature_columns)
    linear_est.train(train_input_fn, steps=100)

    result = linear_est.evaluate(val_input_fn)
    print(result)

    result = linear_est.predict(val_input_fn)
    for pred, exp in zip(result, y_test[:32]):
        print('Predicted Value: ', pred['predictions'][0], 'Expected: ', exp)
