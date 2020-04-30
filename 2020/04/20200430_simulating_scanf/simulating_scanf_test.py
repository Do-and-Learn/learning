import re
import unittest


def scanf(scan_format, input_text):
    """
    %c              --->  .
    %5c             --->  .{5}
    %d              --->  [-+]?\d+
    %e, %E, %f, %g  --->  [-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?
    %i              --->  [-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)
    %o              --->  [-+]?[0-7]+
    %s              --->  \S+
    %u              --->  \d+
    %x, %X          --->  [-+]?(0[xX])?[\dA-Fa-f]+
    """
    pattern = scan_format.replace('%s', r'(\S+)').replace('%d', r'([-+]?\d+)')
    match = re.match(pattern, input_text)
    return match.groups()


class SimulatingScanfTest(unittest.TestCase):

    def test_scanf(self):
        input_text = '/usr/sbin/sendmail - 0 errors, 4 warnings'
        scan_format = '%s - %d errors, %d warnings'
        self.assertCountEqual(('/usr/sbin/sendmail', '0', '4'), scanf(scan_format, input_text))


if __name__ == '__main__':
    unittest.main()
