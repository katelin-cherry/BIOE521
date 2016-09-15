# "+" matches the preceding pattern element one or more times

import re

string1="Hello, world."
if re.search(r"l+", string1):
	print 'There are one or more consecutive letter "l"' +\
		"'s in "  + string1
