import os

import gensim.downloader as api
from gensim.models import Word2Vec

if __name__ == '__main__':
    dataset = api.load("text8")
    model = Word2Vec(dataset)
    os.makedirs('data', exist_ok=True)
    model.save("data/text8-word2vec.bin")
