import unittest
from operator import itemgetter, attrgetter


class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"('{self.name}', '{self.grade}', {self.age})"

    def __eq__(self, other):
        return str(other) == self.__str__()


class SortedTest(unittest.TestCase):

    def test_key_1(self):
        student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
        self.assertEqual([('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)],
                         sorted(student_tuples, key=itemgetter(-1)))

    def test_key_2(self):
        student_tuples = [Student('john', 'A', 15), Student('jane', 'B', 12), Student('dave', 'B', 10)]
        self.assertEqual([('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)],
                         sorted(student_tuples, key=attrgetter('age')))

    def test_key_3(self):
        student_dicts = [{'name': 'john', 'grade': 'A', 'age': 15},
                         {'name': 'jane', 'grade': 'B', 'age': 12},
                         {'name': 'dave', 'grade': 'B', 'age': 10}]
        self.assertEqual([{'name': 'dave', 'grade': 'B', 'age': 10},
                          {'name': 'jane', 'grade': 'B', 'age': 12},
                          {'name': 'john', 'grade': 'A', 'age': 15}],
                         sorted(student_dicts, key=itemgetter('age')))
