import tensorflow as tf
import tensorflow_hub as hub

if __name__ == '__main__':
    module_url = "https://tfhub.dev/google/elmo/2"
    tf.compat.v1.disable_eager_execution()
    elmo = hub.Module(module_url, trainable=False)
    embeddings = elmo([
        "i like green eggs and ham",
        "would you eat them in a box"
    ], signature="default",
        as_dict=True
    )["elmo"]
    print(embeddings.shape)  # (2, 7, 1024)
