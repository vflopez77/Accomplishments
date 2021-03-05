#!/usr/bin/python

import sys

# Get length of passed-in string
maxLength = 59
stringLength = len(str(sys.argv[1]))
charstr = 'character'
print(f'The length of the string "{sys.argv[1]}" is {stringLength}.')
if stringLength >= 59:
    if stringLength == 59:
        charstr = 'character'
    else:
        charstr = 'characters'
    print(f'The string is too long.  Please shorten by {stringLength-maxLength} {charstr}.')
else:
    print(f'The string is not too long.')
