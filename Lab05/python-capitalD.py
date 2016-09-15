
# "\D" - matches a non-digit

import re

string1 = "Hello World"
if re.search(r"\D", string1):
    print "There is at least one character in", string1,
    print "that is not a digit."