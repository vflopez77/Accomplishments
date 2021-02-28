#!/usr/bin/python

import sys

# Get length of passed-in string
stringlength = len(str(sys.argv[1]))
print(f'The length of the string "{sys.argv[1]}" is {stringlength}.')
if stringlength >= 59:
    if stringlength == 59:
        charstr = 'character'
    else:
        charstr = 'characters'
    print(f'The string is too long.  Please shorten by {stringlength-58} {charstr}.')
else:
    print(f'The string is not too long.')
