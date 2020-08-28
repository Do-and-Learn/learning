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

    print_most_similar(model.wv.most_similar('king'), 5)

    # 測試 Paris : France :: Berlin : Germany 為真? 是，結果應回傳 germany
    # Paris 與 France 的距離 應與 Berlin 與 Germany 的距離相近
    #     Paris - France = Berlin - Germany
    # =>  Germany = Berlin - Paris + France
    # =>  正值: Berlin、France；負值: Paris (翻譯成如下)
    print_most_similar(model.wv.most_similar(positive=['berlin', 'france'], negative=['paris']), 1)
    print_most_similar(model.wv.most_similar_cosmul(positive=['berlin', 'france'], negative=['paris']), 1)
