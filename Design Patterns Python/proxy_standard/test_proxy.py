import contextlib
import io
import unittest

from .image import Image, Graphic
from .image_proxy import ImageProxy


class TestProxy(unittest.TestCase):

    def test_image(self) -> None:
        # 確定 Image 物件的 method 被呼叫的時候，被呼叫的 method 會出現在標準輸出中。
        # 以此為基礎，我們在後面的測試中，才可以確定 Proxy (standard) 是否有呼叫 Image 物件的 method。

        image = Image()

        with self.subTest('draw'):
            string_io = io.StringIO()
            with contextlib.redirect_stdout(string_io):
                image.draw()
            self.assertEqual('Image.draw', string_io.getvalue().strip())

        with self.subTest('get_extend'):
            string_io = io.StringIO()
            with contextlib.redirect_stdout(string_io):
                image.get_extend()
            self.assertEqual('Image.get_extend', string_io.getvalue().strip())

        with self.subTest('get_store'):
            string_io = io.StringIO()
            with contextlib.redirect_stdout(string_io):
                image.get_store()
            self.assertEqual('Image.get_store', string_io.getvalue().strip())

        with self.subTest('load'):
            string_io = io.StringIO()
            with contextlib.redirect_stdout(string_io):
                image.load()
            self.assertEqual('Image.load', string_io.getvalue().strip())

    def test_graphic(self):
        self.assertTrue(issubclass(Image, Graphic))

    def test_proxy(self):
        proxy = ImageProxy('xxx.png')

        with self.subTest('Relation between ImageProxy and Image'):
            self.assertTrue(isinstance(proxy, Graphic))
            self.assertTrue(issubclass(ImageProxy, (Graphic,)))
