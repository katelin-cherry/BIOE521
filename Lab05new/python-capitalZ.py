
# "\Z" - matches the end of a string (but not an internal line).

#! /usr/bin/python
import re

string1 = "Hello\nWorld\n"
if re.search(r"d\n\Z", string1):
    print string1, "is a string",
    print "that ends with 'd\\n'"