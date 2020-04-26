import unittest


class Fake(object):
    def __init__(self):
        self._name = ''

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value


class GetterAndSetterTest(unittest.TestCase):

    def test_getter_and_setter_initial(self):
        fake = Fake()
        self.assertEqual('', fake.name)

    def test_getter_and_setter_set_and_get(self):
        fake = Fake()
        fake.name = 'Teddy'
        self.assertEqual('Teddy', fake.name)


if __name__ == '__main__':
    unittest.main()
