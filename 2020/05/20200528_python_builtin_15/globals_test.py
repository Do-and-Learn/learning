import unittest

hi = 'Hello'


class GlobalsTest(unittest.TestCase):

    def test_global_variable(self):
        self.assertIn('hi', globals())
        self.assertEqual('Hello', globals()['hi'])

    def test_modify_variable_will_change_original_variable(self):
        globals()['hi'] = 'Hi Teddy'
        self.assertEqual('Hi Teddy', globals()['hi'])
        self.assertEqual('Hi Teddy', hi)

    def test_local_variable(self):
        person = 'Teddy'
        self.assertNotIn('person', globals())
