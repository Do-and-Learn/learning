import re
import unittest


class MyTestCase(unittest.TestCase):

    def test_example_1(self):
        text = """\
Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""

        entries = re.split("\n+", text)
        self.assertListEqual(['Ross McFluff: 834.345.1254 155 Elm Street',
                              'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
                              'Frank Burger: 925.541.7625 662 South Dogwood Way',
                              'Heather Albrecht: 548.326.4584 919 Park Place'], entries)

    def test_example_2(self):
        entries = [re.split(":? ", entry, 3) for entry in ['Ross McFluff: 834.345.1254 155 Elm Street',
                                                           'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
                                                           'Frank Burger: 925.541.7625 662 South Dogwood Way',
                                                           'Heather Albrecht: 548.326.4584 919 Park Place']]
        self.assertListEqual([['Ross', 'McFluff', '834.345.1254', '155 Elm Street'],
                              ['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'],
                              ['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'],
                              ['Heather', 'Albrecht', '548.326.4584', '919 Park Place']], entries)

    def test_example_3(self):
        entries = [re.split(":? ", entry, 4) for entry in ['Ross McFluff: 834.345.1254 155 Elm Street',
                                                           'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
                                                           'Frank Burger: 925.541.7625 662 South Dogwood Way',
                                                           'Heather Albrecht: 548.326.4584 919 Park Place']]
        self.assertListEqual([['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'],
                              ['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'],
                              ['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'],
                              ['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']], entries)


if __name__ == '__main__':
    unittest.main()
