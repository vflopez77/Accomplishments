#!/usr/bin/python
# Import Library
import sys

# Create the StringText Class
class StringText(object):
    
    # This is the maximum length that can be exported from the outliner without wrapping
    maxLength = 59
    
    # Constructor
    def __init__(self, content):
        self.content = content
        self.length = len(str(content))
        
    # Method to check if string is too long    
    def isTooLong(self):
        if self.length > 59:
            return(True)
        else:
            return(False)
    
    # Method to get absolute character difference
    def charDiff(self):
        return(abs(maxLength-self.length))
    
    # Method to determine if character difference is only one (for pluralization)
    def oneCharOverUnder(self):
        if StringText.charDiff(self) == 1:
            return(True)
        else:
            return(False)
            

# Create instance of the class from the command line parameter
myString = StringText(sys.argv[1])

# Print out the string and its length
print(f'The length of the string "{myString.content}" is {myString.length}. ')

# Case when the string is too long
if myString.isTooLong() == True:
    print(f'The string is too long please shorten by {myString.charDiff()} character', end = '')
    # Checking for a single character difference
    if myString.oneCharOverUnder() == False:
        print('s.')
    else:
        print('.')
        
# Case when the string is not too long
else:
    print(f'The string is not too long with {myString.charDiff()} character', end = '')
    # Checking for a single character difference
    if myString.oneCharOverUnder() == False:
        print('s', end = '')
    print(' to spare.')