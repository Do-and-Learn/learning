import os

import gensim.downloader as api
import numpy as np
import tensorflow as tf


def build_embedding_matrix(word2idx, embedding_dim, embedding_file):
    embedding_model = "glove-wiki-gigaword-300"
    if os.path.exists(embedding_file):
        E = np.load(embedding_file)
    else:
        vocab_size = len(word2idx)
        E = np.zeros((vocab_size, embedding_dim))
        word_vectors = api.load(embedding_model)
        for word, idx in word2idx.items():
            try:
                E[idx] = word_vectors.word_vec(word)
            except KeyError:  # word not in embedding
                pass
        np.save(embedding_file, E)
    return E


def download_and_read(url):
    local_file = url.split('/')[-1]
    tf.keras.utils.get_file(local_file, url, extract=True, cache_dir='.')
    labels, texts = [], []
    local_file = os.path.join('datasets', 'SMSSpamCollection')
    with open(local_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            label, text = line.strip().split('\t')
            labels.append(1 if label == 'spam' else 0)
            texts.append(text)
    return texts, labels


class SpamClassifierModel(tf.keras.Model):

    def __init__(self, vocab_sz, embed_sz, input_length, num_filters, kernel_sz, output_sz, run_mode, embedding_weights, **kwargs):
        super(SpamClassifierModel, self).__init__(**kwargs)
        if run_mode == 'scratch':
            self.embedding = tf.keras.layers.Embedding(vocab_sz, embed_sz, input_length=input_length, trainable=True)
        elif run_mode == 'vectorizer':
            self.embedding = tf.keras.layers.Embedding(vocab_sz, embed_sz, input_length=input_length, weights=[embedding_weights], trainable=False)
        else:  # finetuning
            self.embedding = tf.keras.layers.Embedding(vocab_sz, embed_sz, input_length=input_length, weights=[embedding_weights], trainable=True)
        self.conv = tf.keras.layers.Conv1D(filters=num_filters, kernel_size=kernel_sz, activation="relu")
        self.dropout = tf.keras.layers.SpatialDropout1D(0.2)
        self.pool = tf.keras.layers.GlobalMaxPooling1D()
        self.dense = tf.keras.layers.Dense(output_sz, activation="softmax")

    def call(self, inputs, training=None, mask=None):
        x = self.embedding(inputs)
        x = self.conv(x)
        x = self.dropout(x)
        x = self.pool(x)
        x = self.dense(x)
        return x

    def get_config(self):
        pass


if __name__ == '__main__':
    texts, labels = download_and_read('https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip')

    # tokenize and pad text
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(texts)
    text_sequences = tokenizer.texts_to_sequences(texts)
    text_sequences = tf.keras.preprocessing.sequence.pad_sequences(text_sequences)

    # labels
    NUM_CLASSES = 2
    cat_labels = tf.keras.utils.to_categorical(labels, num_classes=NUM_CLASSES)

    # dataset
    dataset = tf.data.Dataset.from_tensor_slices((text_sequences, cat_labels))
    dataset = dataset.shuffle(10000)

    num_records = len(text_sequences)
    test_size = num_records // 4  # get int part
    val_size = (num_records - test_size) // 10

    test_dataset = dataset.take(test_size)
    val_dataset = dataset.skip(test_size).take(val_size)
    train_dataset = dataset.skip(test_size + val_size)

    BATCH_SIZE = 128
    test_dataset = test_dataset.batch(BATCH_SIZE, drop_remainder=True)
    val_dataset = val_dataset.batch(BATCH_SIZE, drop_remainder=True)
    train_dataset = train_dataset.batch(BATCH_SIZE, drop_remainder=True)

    EMBEDDING_DIM = 300
    DATA_DIR = 'data'
    os.makedirs(DATA_DIR, exist_ok=True)
    EMBEDDING_NUMPY_FILE = os.path.join(DATA_DIR, 'E.npy')
    E = build_embedding_matrix(tokenizer.word_index, EMBEDDING_DIM, EMBEDDING_NUMPY_FILE)

    conv_num_filters = 256
    conv_kernel_size = 3
    run_mode = 'scratch'
    model = SpamClassifierModel(len(tokenizer.word_index), EMBEDDING_DIM, len(text_sequences[0]), conv_num_filters, conv_kernel_size, NUM_CLASSES, run_mode, E)
    model.build(input_shape=(None, len(text_sequences[0])))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # dataset
    dataset = tf.data.Dataset.from_tensor_slices((text_sequences, cat_labels))
    dataset = dataset.shuffle(10000)
    test_size = num_records // 4
    val_size = (num_records - test_size) // 10
    test_dataset = dataset.take(test_size)
    val_dataset = dataset.skip(test_size).take(val_size)
    train_dataset = dataset.skip(test_size + val_size)

    test_dataset = test_dataset.batch(BATCH_SIZE, drop_remainder=True)
    val_dataset = val_dataset.batch(BATCH_SIZE, drop_remainder=True)
    train_dataset = train_dataset.batch(BATCH_SIZE, drop_remainder=True)

    # compile and train
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    # train model
    NUM_EPOCHS = 3
    CLASS_WEIGHTS = {0: 1, 1: 8}
    model.fit(train_dataset, epochs=NUM_EPOCHS, validation_data=val_dataset, class_weight=CLASS_WEIGHTS)
