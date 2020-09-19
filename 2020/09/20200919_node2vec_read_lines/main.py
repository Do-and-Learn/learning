import tensorflow as tf


def download_and_read(url):
    local_file = url.split('/')[-1]  # local_file = 'NIPS_1987-2015.csv'

    # download file from url and save it to /datasets/NIPS_1987-2015.csv
    # it will not download the file if the file already there
    p = tf.keras.utils.get_file(local_file, url, cache_dir='.')  # p = '.\datasets\NIPS_1987-2015.csv'

    with open(p, 'r') as f:
        for line in f:
            line = line.strip()
            print(line)


if __name__ == '__main__':
    download_and_read('https://archive.ics.uci.edu/ml/machine-learning-databases/00371/NIPS_1987-2015.csv')
