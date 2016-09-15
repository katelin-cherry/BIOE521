# "\b" - Matches a word boundary

#! /usr/bin/python



import re

string1 = "Hello World"
if re.search(r"llo\b", string1):
    print "There is a word that ends with 'llo'"
else:
    print "There are no words that end with 'llo'"
