# "\s" matches a whitespace character (space, tab, newline, formfeed)
#! /usr/bin/python

import re

string1= "Hello World\n"

if re.search(r"\s.*\s",string1):
	print "There are TWO whitespace characters, which may"
	print "be separated by other characters, in", string1
