from tensorflow.keras.applications.inception_v3 import InceptionV3


def print_layer(_layer):
    print(f'{type(_layer).__name__}')
    print(f'    name:         {_layer.name}')
    print(f'    input_shape:  {_layer.input_shape}')
    print(f'    output_shape: {_layer.output_shape}')


if __name__ == '__main__':
    # create the base pre-trained model
    base_model = InceptionV3(weights='imagenet', include_top=False)

    print('[ last four layers (include_top=False) ]'.center(80, '-'))
    for layer in base_model.layers[-4:]:
        print_layer(layer)

    # create the base pre-trained model
    base_model = InceptionV3(weights='imagenet', include_top=True)

    print('[ last four layers (include_top=True) ]'.center(80, '-'))
    for layer in base_model.layers[-4:]:
        print_layer(layer)
