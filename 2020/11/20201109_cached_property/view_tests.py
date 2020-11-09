import contextlib
import io
import unittest

from view1 import View1


class ViewTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.view1 = View1()

    def test_cached_property(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            _ = self.view1.component1
            _ = self.view1.component1
            _ = self.view1.component1
        self.assertEqual('build component1 (View1)\n', f.getvalue())

    def test_cached_property2(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            _ = self.view1.component1
            _ = self.view1.component1
            _ = self.view1.component1
            _ = self.view1.component2
            _ = self.view1.component2
            _ = self.view1.component3
            _ = self.view1.component3
        self.assertEqual('build component1 (View1)\n'
                         'build component2 (View1)\n'
                         'build component3 (View1)\n', f.getvalue())
