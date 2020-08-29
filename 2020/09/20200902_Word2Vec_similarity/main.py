import os

import gensim.downloader as api
from gensim.models import Word2Vec, KeyedVectors

if __name__ == '__main__':
    bin_file_path = 'data/text8-word2vec.bin'

    if not os.path.exists(bin_file_path):
        dataset = api.load('text8')
        model = Word2Vec(dataset)
        os.makedirs('data', exist_ok=True)
        model.save(bin_file_path)

    model = KeyedVectors.load(bin_file_path)

    base_word = 'man'
    for word in ['woman', 'dog', 'whale', 'tree']:
        print(f'similarity({base_word}, {word}) = {model.wv.similarity(base_word, word):.3f}')
