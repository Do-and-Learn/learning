import tensorflow_datasets as tfds

if __name__ == '__main__':
    # https://www.tensorflow.org/datasets/catalog/cycle_gan#cycle_gansummer2winter_yosemite

    """
    The following statement will raise an exception:
      tensorflow_datasets.core.download.extractor.ExtractError: Error while extracting ... : 'utf-8' codec can't decode byte 0xc0 in position 290: invalid start byte
    """
    dataset, metadata = tfds.load('cycle_gan/summer2winter_yosemite', with_info=True, as_supervised=True)
