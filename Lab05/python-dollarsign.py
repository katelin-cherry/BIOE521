
# "$" - matches the end of a line or string

import re

string1 = "Hello World"
if re.search(r"rld$", string1):
    print string1, "is a line or string " +\
          "that ends with 'rld'"