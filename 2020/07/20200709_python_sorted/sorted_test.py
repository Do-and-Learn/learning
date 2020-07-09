import unittest


class SortedTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual([1, 2, 3, 4, 5], sorted([5, 2, 3, 1, 4]))
        self.assertEqual([1, 2, 3, 4, 5], sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

    def test_key(self):
        self.assertEqual(['a', 'Andrew', 'from', 'is', 'string', 'test', 'This'],
                         sorted("This is a test string from Andrew".split(), key=str.lower))

    def test_key_2(self):
        student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
        self.assertEqual([('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)],
                         sorted(student_tuples, key=lambda student: student[-1]))

    def test_key_3(self):
        student_dicts = [{'name': 'john', 'grade': 'A', 'age': 15},
                         {'name': 'jane', 'grade': 'B', 'age': 12},
                         {'name': 'dave', 'grade': 'B', 'age': 10}]
        self.assertEqual([{'name': 'dave', 'grade': 'B', 'age': 10},
                          {'name': 'jane', 'grade': 'B', 'age': 12},
                          {'name': 'john', 'grade': 'A', 'age': 15}],
                         sorted(student_dicts, key=lambda student: student['age']))
