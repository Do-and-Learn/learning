import csv
import os

import numpy as np
import scipy
import tensorflow as tf
from scipy.sparse import csr_matrix


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
        for i in range(E.shape[0]):  # for each vertex E.shape[0] = 5811
            if i % 100 == 0:
                print(f'{n * i} random walks generated from {i} vertices')
            for j in range(n):  # n random walks
                curr = i
                walk = [curr]
                target_nodes = np.nonzero(E[curr])[1]
                print(target_nodes)
                break
            break


if __name__ == '__main__':
    npz = 'NIPS_1987-2015.npz'
    npy = 'E.npz'
    if not os.path.exists(npy):
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
        scipy.sparse.save_npz(npy, E)
    else:
        E = scipy.sparse.load_npz(npy)

    NUM_WALKS_PER_VERTEX = 32
    MAX_PATH_LENGTH = 40
    RESTART_PROB = 0.15
    RANDOM_WALKS_FILE = os.path.join('data', 'random-walk.txt')

    construct_random_walks(E, NUM_WALKS_PER_VERTEX, RESTART_PROB, MAX_PATH_LENGTH, RANDOM_WALKS_FILE)
