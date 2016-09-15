# "\W" - matches an non- alphanumeric character, excluding "_"

#! /usr/bin/python
import re

string1= "Hello, world."
if re.search(r"\W", string1):
	print "The space between Hello and " +\
		"World is not alphanumeric"
