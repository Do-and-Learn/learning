import unittest


class Person:
    @classmethod
    def hi(cls, name: str):
        return f'{cls.__name__}: Hi, {name}'


class Man(Person):
    pass


class ClassMethodTest(unittest.TestCase):

    def test_classmethod(self):
        self.assertEqual(Person.hi('Teddy'), 'Person: Hi, Teddy')
        self.assertEqual(Person().hi('Claire'), 'Person: Hi, Claire')

    def test_classmethod_derived_class(self):
        self.assertEqual(Man.hi('Teddy'), 'Man: Hi, Teddy')


if __name__ == '__main__':
    unittest.main()
