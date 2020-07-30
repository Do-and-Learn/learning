import numpy as np
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image
from tensorflow.python.keras.applications.vgg16 import VGG16, preprocess_input

if __name__ == '__main__':
    base_model = VGG16(weights='imagenet', include_top=True)

    for i, layer in enumerate(base_model.layers):
        print(i, layer.name, layer.output_shape)

    model = models.Model(inputs=base_model.input, outputs=base_model.get_layer('block4_pool').output)
    img_path = 'cat.jpg'
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    features = model.predict(x)
    print(features)
