import numpy as np
import tensorflow as tf

((train_data, train_labels), (test_data, test_labels)) = tf.keras.datasets.mnist.load_data()

train_data = train_data / np.float32(255)
train_labels = train_labels.astype(np.int32)

test_data = test_data / np.float32(255)
test_labels = test_labels.astype(np.int32)

feature_columns = [tf.feature_column.numeric_column('x', shape=[28, 28])]

classifier = tf.estimator.LinearClassifier(feature_columns=feature_columns, n_classes=10, model_dir='mnist_model/')

train_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
    x={'x': train_data},
    y=train_labels,
    batch_size=100,
    num_epochs=None,
    shuffle=True
)

classifier.train(input_fn=train_input_fn, steps=130)

test_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
    x={'x': test_data},
    y=test_labels,
    num_epochs=1,
    shuffle=False
)

test_result = classifier.evaluate(input_fn=test_input_fn)
print(test_result)
