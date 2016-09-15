
# "{M,N}" denotes the minimum M and the maximum N match count
#! /usr/bin/python
import re

string1= "Hello, world."

if re.search (r"l{1,2}", string1):
	print "There exists a substring with at least l\n" +\
		"and at most 2 l's in " + string1
