import contextlib
import io
import unittest

from view1 import View1
from view2 import View2


class ViewTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.view1 = View1()
        self.view2 = View2()

    def test_wait_for_view(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            _ = self.view1.component1
            _ = self.view1.component1
            _ = self.view1.component1
        self.assertEqual('wait for view 1\n'
                         'build component1 (View1)\n', f.getvalue())

    def test_wait_for_view_2(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            _ = self.view1.component1
            _ = self.view1.component1
            _ = self.view1.component1
            _ = self.view1.component2
            _ = self.view1.component2
            _ = self.view1.component3
            _ = self.view1.component3
        self.assertEqual('wait for view 1\n'
                         'build component1 (View1)\n'
                         'build component2 (View1)\n'
                         'build component3 (View1)\n', f.getvalue())

    def test_wait_for_view_3(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            _ = self.view1.component1
            _ = self.view2.component1
            _ = self.view1.component2
            _ = self.view1.component3
            _ = self.view2.component2
            _ = self.view2.component3
        self.assertEqual('wait for view 1\n'
                         'build component1 (View1)\n'
                         'wait for view 2\n'
                         'build component1 (View2)\n'
                         'build component2 (View1)\n'
                         'build component3 (View1)\n'
                         'build component2 (View2)\n'
                         'build component3 (View2)\n', f.getvalue())
