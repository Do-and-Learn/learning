import os

import gensim.downloader as api
from gensim.models import Word2Vec, KeyedVectors


def print_most_similar(word_conf_pairs, k):
    for i, (word, conf) in enumerate(word_conf_pairs):
        print(f'{conf:.3f} {word}')
        if i >= k - 1:
            break
    if k < len(word_conf_pairs):
        print('...')


if __name__ == '__main__':
    bin_file_path = 'data/text8-word2vec.bin'

    if not os.path.exists(bin_file_path):
        dataset = api.load('text8')
        model = Word2Vec(dataset)
        os.makedirs('data', exist_ok=True)
        model.save(bin_file_path)

    model = KeyedVectors.load(bin_file_path)

    print(print_most_similar(model.wv.similar_by_word("taipei"), 5))
