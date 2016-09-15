#! /usr/bin/python

import sys
import re

for arg in sys.argv:
#	print arg
	string1=arg
	if re.search(r".....",string1):
		print string1+" has length >=5"

