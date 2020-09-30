import csv
import os

import gensim
import numpy as np
import scipy
import tensorflow as tf
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity


# noinspection PyTypeChecker


def download_and_read(url):
    local_file = url.split('/')[-1]  # local_file = 'NIPS_1987-2015.csv'

    # download file from url and save it to /datasets/NIPS_1987-2015.csv
    # it will not download the file if the file already there
    p = tf.keras.utils.get_file(local_file, url, cache_dir='.')  # p = '.\datasets\NIPS_1987-2015.csv'

    data = []
    row_ids = []
    col_ids = []

    with open(p, 'r') as f:
        rows = csv.reader(f)
        _ = next(rows)  # header
        for rid, row in enumerate(rows):
            counts = np.array([int(cell) for cell in row[1:]])
            nz_col_ids = np.nonzero(counts)[0]  # sparse matrix
            nz_data = counts[nz_col_ids]
            nz_row_ids = np.repeat(rid, len(nz_col_ids))
            data.extend(nz_data.tolist())
            row_ids.extend(nz_row_ids.tolist())
            col_ids.extend(nz_col_ids.tolist())

    return csr_matrix((np.array(data), (np.array(row_ids), np.array(col_ids))), shape=(len(data), counts.shape[0]))  # csr(compressed sparse row matrix)


def construct_random_walks(E, n, alpha, l, ofile):
    if os.path.exists(ofile):
        print('random walks generated already, skipping')
    else:
        with open(ofile, 'w') as f:
            for i in range(E.shape[0]):  # for each vertex E.shape[0] = 5811
                if i % 100 == 0:
                    print(f'{n * i} random walks generated from {i} vertices')
                for j in range(n):  # n random walks
                    curr = i
                    walk = [curr]
                    target_nodes = np.nonzero(E[curr])[1]
                    for k in range(l):
                        if np.random.random() < alpha and len(walk) > 5:
                            break
                        curr = np.random.choice(target_nodes)
                        walk.append(curr)
                        target_nodes = np.nonzero(E[curr])[1]
                    f.write(f'{" ".join([str(x) for x in walk])}\n')


class Documents(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def __iter__(self):
        with open(self.input_file, 'r') as f:
            for i, line in enumerate(f):
                if i % 1000 == 0:
                    print(f'{i} random walks extracted')
                yield line.strip().split()


def train_word2vec_model(random_walk_file, model_file):
    if os.path.exists(model_file):
        print(f'Model file {model_file} already present, skipping training')
    else:
        docs = Documents(random_walk_file)
        model = gensim.models.Word2Vec(
            docs,
            size=128,  # size of embedding vector
            window=10,  # window size
            sg=1,  # skip-gram model
            min_count=2,
            workers=4
        )
        model.train(docs, total_examples=model.corpus_count, epochs=50)
        model.save(model_file)


def evaluate_model(td_matrix, model_file, source_id):
    # td_matrix = np.array(td_matrix).astype(np.float)
    model = gensim.models.Word2Vec.load(model_file).wv
    most_similar = model.most_similar(str(source_id))
    scores = [x[1] for x in most_similar]
    target_ids = [int(x[0]) for x in most_similar]
    # compare top 10 scores with cosine similarity between source and each target
    X = np.repeat(td_matrix[source_id].todense(), 10, axis=0)
    Y = td_matrix[target_ids].todense()
    cosims = [cosine_similarity(X[i], Y[i])[0, 0] for i in range(10)]
    for i in range(10):
        print(F'{source_id} {target_ids[i]} {cosims[i]:.3F} {scores[i]:.3f}')


if __name__ == '__main__':
    npz = 'NIPS_1987-2015.npz'
    E_npy = 'E.npz'
    if not os.path.exists(E_npy):
        if not os.path.exists(npz):
            TD = download_and_read('https://archive.ics.uci.edu/ml/machine-learning-databases/00371/NIPS_1987-2015.csv')
            scipy.sparse.save_npz(npz, TD)
        else:
            TD = scipy.sparse.load_npz(npz)

        # shape:
        #    E    (5811, 5811)
        #    TD   (4033830, 5811)
        #    TD.D (5811, 4033830)
        E = TD.T * TD  # edge matrix
        E[E > 0] = 1
        scipy.sparse.save_npz(E_npy, E)
    else:
        E = scipy.sparse.load_npz(E_npy)
        TD = scipy.sparse.load_npz(npz)

    NUM_WALKS_PER_VERTEX = 32
    MAX_PATH_LENGTH = 40
    RESTART_PROB = 0.15
    RANDOM_WALKS_FILE = os.path.join('data', 'random-walks.txt')
    os.makedirs('data', exist_ok=True)

    construct_random_walks(E, NUM_WALKS_PER_VERTEX, RESTART_PROB, MAX_PATH_LENGTH, RANDOM_WALKS_FILE)

    W2V_MODEL_FILE = os.path.join('data', 'w2v-neurips-papers.model')

    # train model
    train_word2vec_model(RANDOM_WALKS_FILE, W2V_MODEL_FILE)

    source_id = np.random.choice(E.shape[0])
    evaluate_model(TD, W2V_MODEL_FILE, source_id)
