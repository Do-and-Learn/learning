import re
import unittest
from typing import NamedTuple, Any


class Token(NamedTuple):
    type: str
    value: Any
    line: int
    column: int


def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER', r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN', r':='),  # Assignment operator
        ('END', r';'),  # Statement terminator
        ('ID', r'[A-Za-z]+'),  # Identifiers
        ('OP', r'[+\-*/]'),  # Arithmetic operators
        ('NEWLINE', r'\n'),  # Line endings
        ('SKIP', r'[ \t]+'),  # Skip over spaces and tabs
        ('MISMATCH', r'.'),  # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup  # The name of the last matched capturing group, or None if the group didn’t have a name, or if no group was matched at all.
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)


class ExampleTest(unittest.TestCase):
    def test_example(self):
        statements = '''
            IF quantity THEN
                total := total + price * quantity;
                tax := price * 0.05;
            ENDIF;
        '''
        self.assertCountEqual([
            Token(type='IF', value='IF', line=2, column=12),
            Token(type='ID', value='quantity', line=2, column=15),
            Token(type='THEN', value='THEN', line=2, column=24),

            Token(type='ID', value='total', line=3, column=16),
            Token(type='ASSIGN', value=':=', line=3, column=22),
            Token(type='ID', value='total', line=3, column=25),
            Token(type='OP', value='+', line=3, column=31),
            Token(type='ID', value='price', line=3, column=33),
            Token(type='OP', value='*', line=3, column=39),
            Token(type='ID', value='quantity', line=3, column=41),
            Token(type='END', value=';', line=3, column=49),

            Token(type='ID', value='tax', line=4, column=16),
            Token(type='ASSIGN', value=':=', line=4, column=20),
            Token(type='ID', value='price', line=4, column=23),
            Token(type='OP', value='*', line=4, column=29),
            Token(type='NUMBER', value=0.05, line=4, column=31),
            Token(type='END', value=';', line=4, column=35),

            Token(type='ENDIF', value='ENDIF', line=5, column=12),
            Token(type='END', value=';', line=5, column=17)
        ], [token for token in tokenize(statements)])


if __name__ == '__main__':
    unittest.main()
