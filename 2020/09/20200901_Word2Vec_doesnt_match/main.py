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

    # hindus (印度教) parsis (帕西人，一個信仰瑣羅亞斯德教的民族) singapore (新加坡) christians (基督徒)
    # will get a message:
    #   site-packages\gensim\models\keyedvectors.py:877: FutureWarning: arrays to stack must be passed as a "sequence" type such as list or tuple. Support for non-sequence iterables such as generators is deprecated as of NumPy 1.16 and will raise an error in the future.
    #   vectors = vstack(self.word_vec(word, use_norm=True) for word in used_words).astype(REAL)

    print(model.wv.doesnt_match(["hindus", "parsis", "singapore", "christians"]))
