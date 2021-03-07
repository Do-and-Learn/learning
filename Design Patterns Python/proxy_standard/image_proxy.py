from __future__ import annotations

from .image import Graphic


class ImageProxy(Graphic):

    def __init__(self, image_path: str):
        self.__image_path = image_path
