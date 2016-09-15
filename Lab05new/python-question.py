#! /usr/bin/python

import re

string1 = "Hello, world."
if re.search(r"H.?e", string1):
	print "There is an 'H' an a 'e' separated by " +\
		"0-1 characters (Ex: He Hoe) \n" 
