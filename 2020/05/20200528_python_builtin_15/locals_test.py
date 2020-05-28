import unittest

hi = 'Hello'


class LocalsTest(unittest.TestCase):

    def test_global_variable(self):
        self.assertNotIn('hi', locals())

    def test_local_variable(self):
        person = 'Teddy'
        self.assertIn('person', locals())
        self.assertIn('Teddy', locals()['person'])

    def test_modify_variable_not_change_original_variable(self):
        person = 'Teddy'
        locals()['person'] = 'Claire'
        self.assertEqual('Teddy', locals()['person'])
