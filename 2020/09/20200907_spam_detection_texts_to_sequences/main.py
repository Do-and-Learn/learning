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
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(texts)
    text_sequences = tokenizer.texts_to_sequences(texts)
    for text_sequence, text in zip(text_sequences, texts):
        print(f'sequence("{text}") = {text_sequence}')
