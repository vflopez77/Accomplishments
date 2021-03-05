#!/usr/bin/python
import sys

# Get length of passed-in string
maxLength = 59
stringLength = len(str(sys.argv[1]))
charstr = 'character'
# Report length of string
print(f'The length of the string "{sys.argv[1]}" is {stringLength}.')

# Test length of string and report string is too long
if stringLength > maxLength:
    if stringLength-maxLength != 1:
        print(f'The string is too long.  Please shorten by {stringLength-maxLength} {charstr}s.')
    else:
        print(f'The string is too long.  Please shorten by {stringLength-maxLength} {charstr}.')
# Report string is not too long
elif abs(stringLength-maxLength) != 1:
    print(f'The string is not too long with {abs(stringLength-maxLength)} {charstr}s to spare.')
else: # A single character under
    print(f'The string is not too long with {abs(stringLength-maxLength)} {charstr} to spare.')
