# "\w" - Matches an alphanumeric character, including "_".
#! /usr/bin/python

import re

string1 = "Hello World"
m_obj = re.search(r"(\w\w)", string1)
if m_obj:
    print "The first two adjacent alphanumeric characters"
    print "(A-Z, a-z, 0-9, _) in", string1, "were",
    print m_obj.group(1)

