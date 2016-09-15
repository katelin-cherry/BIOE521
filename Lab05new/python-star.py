
# "*" matches the preceding pattern element zero or more times
#! /usr/bin/python
import re

string1= "Hello, world."

if re.search (r"el*o", string1):
	print "There is an 'e' followed by zero to many\n" +\
		"'l' followed by 'o' (eo,elo,ello,elllo)"
