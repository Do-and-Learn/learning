class Graphic:

    def draw(self):
        pass

    def get_extend(self):
        pass

    def get_store(self):
        pass

    def load(self):
        pass


class Image(Graphic):

    def draw(self):
        print('Image.draw')

    def get_extend(self):
        print('Image.get_extend')

    def get_store(self):
        print('Image.get_store')

    def load(self):
        print('Image.load')
