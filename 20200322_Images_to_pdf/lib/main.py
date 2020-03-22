from enum import Enum


class PageSpec(Enum):
    A4 = {'width': 210, 'height': 297}

    @property
    def width(self):
        return self.value['width']

    @property
    def height(self):
        return self.value['height']