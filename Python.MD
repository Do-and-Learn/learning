# The Python Standard Library

## [Built-in Functions](https://docs.python.org/3/library/functions.html)

|  |  |  |  |  |
| -- | -- | -- | -- | -- |
| [abs()](2020/05/20200512_builtin_2/abs_test.py) | delattr() | hash() | memoryview() | set() |
| [all()](2020/05/20200511_builtin_1/all_test.py) | dict() | help() | min() | setattr() |
| [any()](2020/05/20200513_builtin_3/any_test.py) | dir() | hex() | next() | slice() |
| [ascii()](2020/05/20200514_builtin_4/ascii_test.py) | divmod() | id() | object() | sorted() |
| [bin()](2020/05/20200514_builtin_4/bin_test.py) | enumerate() | input() | oct() | staticmethod() |
| [bool()](2020/05/20200514_builtin_4/bool_test.py) | eval() | int() | open() | str() |
| breakpoint() | exec() | isinstance() | ord() | sum() |
| bytearray() | filter()  | issubclass() | pow() | super() |
| bytes() | float() | iter() | print() | tuple() |
| [callable()](2020/05/20200515_builtin_5/callable_test.py) | format() | len() | property() | type() |
| chr() | frozenset() | list() | range() | vars() |
| classmethod() | getattr() | locals() | repr() | zip() |
| compile() | globals() | map() | reversed() | \_\_import\_\_() |
| complex() | hasattr() | max() | round() |

## [Text Processing Services](https://docs.python.org/3/library/text.html)

### string - Common string operations

- :construction: String constants
- :construction: Custom String Formatting
- Format String Syntax
  - :construction: Format Specification Mini-Language
  - :construction: Format examples
- :construction: Template strings
- :construction: Helper functions

### [re](https://docs.python.org/3/library/re.html) - Regular expression operations

- :construction: Regular Expression Syntax
- :construction: Module Contents
- :construction: Regular Expression Objects
- :construction: Match Objects
- Regular Expression Examples
  - [Checking for a Pair](2020/04/20200429_checking_for_a_pair/checking_for_a_pair_test.py)
  - [Simulating scanf()](2020/04/20200430_simulating_scanf/simulating_scanf_test.py)
  - [search() vs. match()](2020/05/20200501_search_vs_match/search_vs_match_test.py)
  - [Making a Phonebook](2020/05/20200502_making_a_phonebook/making_a_phonebook_test.py)
  - [Text Munging](2020/05/20200503_text_munging/text_munging_test.py)
  - [Finding all Adverbs](2020/05/20200504_finding_all_adverbs/finding_all_adverbs_test.py)
  - [Finding all Adverbs and their Positions](2020/05/20200506_finding_all_adverbs_and_their_positions/example_test.py)
  - [Raw String Notation](2020/05/20200507_raw_string_notation/example_test.py)
  - [Writing a Tokenizer](2020/05/20200508_writing_a_tokenizer/example_test.py)

### difflib - Helpers for computing deltas

### [textwrap](https://docs.python.org/3/library/textwrap.html) - Text wrapping and filling

- :construction: class TextWrapper
- [wrap](2020/04/20200427_wrap/wrap_test.py)
- [fill](2020/04/20200428_textwrap_2/fill_test.py)
- [shorten](2020/04/20200428_textwrap_2/shorten_test.py)
- [dedent](2020/04/20200428_textwrap_2/dedent_test.py)
- [indent](2020/04/20200428_textwrap_2/indent_test.py)

### unicodedata - Unicode Database

### stringprep - Internet String Preparation

### readline - GNU readline interface

### rlcompleter - Completion function for GNU readline

# Python mock

[Official Page](https://docs.python.org/3/library/unittest.mock.html)

- [QuickGuide](2020/04/20200418_Python_Mock_Quick_Guide/quick_guide_test.py)
- Mock Class
  - Classes
    - Mock
      - [Assertions](2020/04/20200419_Python_Mock_assertions/mock_class_test.py)
      - [Methods](2020/04/20200421_Python_Mock_methods/mock_test.py)
    - :construction: MagicMock
    - :construction: NonCallableMock
    - :construction: PropertyMock
    - :construction: AsyncMock
  - [Calling](2020/04/20200422_Calling/calling_test.py)
  - [Deleting Attributes](2020/04/20200423_Deleting_Attributes/deleting_attributes_test.py)
  - [Mock names and the name attribute](2020/04/20200424_Mock_Names_And_The_Name_Attribute/mock_name_and_the_name_attribute_test.py)
  - [Attaching Mocks as Attributes](2020/04/20200425_Attaching_Mocks_As_Attributes/attaching_mocks_as_attributes_test.py)
- :construction: Patchers
- :construction: MagicMock
- :construction: Helpers
