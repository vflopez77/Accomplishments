#!/usr/bin/python
# Import Library
import sys

# Create the StringText Class
class StringText(object):
    
    # Constructor
    def __init__(self, content):
        self.content = content
        self.length = len(str(content))
        # This is the maximum length that can be exported from the outliner without wrapping
        self.maxLength = 59
        
    # Method to check if string is too long    
    def isTooLong(self):
        if self.length > self.maxLength:
            return(True)
        else:
            return(False)
    
    # Method to get absolute character difference
    def charDiff(self):
        return(abs(self.maxLength-self.length))
    
    # Method to determine if character difference is only one (for pluralization)
    def oneCharOverUnder(self):
        if StringText.charDiff(self) == 1:
            return(True)
        else:
            return(False)
            
# * This is where the program is actually run *

# Capture string to test
strStringToTest = input("Please input string to test: ")

# Create instance of the class from the command line parameter
myString = StringText(strStringToTest)

# Print out the string and its length
print(f'The length of the string "{myString.content}" is {myString.length}. ')

# Case when the string is too long
if myString.isTooLong() == True:
    print(f'The string is too long.  Please shorten by {myString.charDiff()} character', end = '')
    # Checking for a single character difference for correct pluralization
    if myString.oneCharOverUnder() == False:
        print('s.')
    else:
        print('.')
        
# Case when the string is not too long
else:
    print(f'The string is not too long, with {myString.charDiff()} character', end = '')
    # Checking for a single character difference for correct pluralization
    if myString.oneCharOverUnder() == False:
        print('s', end = '')
    print(' to spare.')