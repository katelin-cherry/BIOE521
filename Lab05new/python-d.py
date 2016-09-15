
# "\d" - matches a digit, same as [0-9]
#! /usr/bin/python
import re

string1 = "99 bottles of beer on the wall."
m_obj = re.search(r"(\d+)", string1)
if m_obj:
    print m_obj.group(1), "is the first number in '" +\
                          string1 + "'"