import unittest


class VarsTest(unittest.TestCase):

    def test_normal_case(self):
        class Person:
            def __init__(self, name, sex):
                self.name = name
                self.sex = sex

        self.assertEqual({'name': 'Teddy', 'sex': 'man'}, vars(Person("Teddy", "man")))

    def test_no_dict_method(self):
        with self.assertRaises(TypeError) as context:
            self.assertEqual({}, vars(object()))
        self.assertEqual("vars() argument must have __dict__ attribute", context.exception.args[0])
