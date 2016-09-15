
# "\S" - matches anything but white space


import re


string1 = "Hello World\n"
m_obj = re.search(r"(\S*)\s*(\S*)", string1)
if m_obj:
    print "The first two groups of NON-whitespace characters"
    print "are '%s' and '%s'." % m_obj.groups()