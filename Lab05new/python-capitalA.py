
# "\A" - matches the beginning of a string (but not an internal line).
#! /usr/bin/python

import re

string1 = "Hello\nWorld\n"
if re.search(r"\AH", string1):
    print string1, "is a string",
    print "that starts with 'H'"