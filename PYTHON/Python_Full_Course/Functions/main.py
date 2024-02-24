# 1/16/24

"""
A regular expression is a special sequence of characters that helps you match
or find other strings or sets of strings, using a specialized syntax held in a pattern. 
A regular expression also known as regex is a sequence of characters that defines a search pattern. 
Popularly known as as regex or regexp; it is a sequence of characters that specifies a match 
pattern in text. Usually, such patterns are used by string-searching algorithms for "find" or 
"find and replace" operations on strings, or for input validation.
Python's standard library has 're' module for this purpose.
"""

import re

first_string = "My name is Ashton Mahatoo!!"

match_pattern = re.compile(r'name')
match_string = match_pattern.finditer(first_string)
for match in match_string:
    print(match)

