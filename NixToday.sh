#!/usr/local/bin/bash

# Simple script to clean up Today.txt file for rerunning
# Have to run script as sudo
# chmod 755 /Users/victor/Downloads/Today.txt
# Use pattern to delete all Today files 
find /Users/victor/Downloads -type f -name 'Today*.txt' -delete