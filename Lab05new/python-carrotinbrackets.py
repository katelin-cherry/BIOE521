
# "[^...]" - matches every character except the ones inside brackets
#! /usr/bin/python
import re

string1 = "Hello World\n"
if re.search(r"[^abc]", string1):
    print string1 + " contains a character other than " +\
          "a, b, and c"