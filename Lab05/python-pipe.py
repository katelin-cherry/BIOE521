# "|" matches the preceding pattern element one or more times

import re

string1 = "Hello, world."
if re.search(r"(Hello|Hi|Pogo)", string1):
    print "At least one of Hello, Hi, or Pogo is " +\
          "contained in " + string1
