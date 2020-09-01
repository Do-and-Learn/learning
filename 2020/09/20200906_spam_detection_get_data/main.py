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
    for label, text in zip(labels, texts):
        print(f'{label}: {text}')
