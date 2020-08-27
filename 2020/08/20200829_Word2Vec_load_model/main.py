import os

import gensim.downloader as api
from gensim.models import Word2Vec, KeyedVectors

if __name__ == '__main__':
    bin_file_path = 'data/text8-word2vec.bin'
    if not os.path.exists(bin_file_path):
        dataset = api.load("text8")
        model = Word2Vec(dataset)
        os.makedirs('data', exist_ok=True)
        model.save(bin_file_path)
    model = KeyedVectors.load(bin_file_path)
    word_vectors = model.wv
    words = word_vectors.vocab.keys()
    print([x for i, x in enumerate(words) if i < 10])
