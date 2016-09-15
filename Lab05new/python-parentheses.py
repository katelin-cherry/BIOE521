
#! /usr/bin/python

import re

string1="Hello, world."
m_obj = re.search(r"(H..).(o..)", string1)
if m_obj:
	print "We matched '" + m_obj.group(1) +\
	"'and'" + m_obj.group(2) +"'"
