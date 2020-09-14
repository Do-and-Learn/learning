import json
import os

import tensorflow as tf


# noinspection PyShadowingNames
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

    # vocabulary
    word2idx = tokenizer.word_index
    print(json.dumps(word2idx, indent=2))