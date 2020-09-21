import csv

import numpy as np
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


if __name__ == '__main__':
    TD = download_and_read('https://archive.ics.uci.edu/ml/machine-learning-databases/00371/NIPS_1987-2015.csv')
    print(TD)
