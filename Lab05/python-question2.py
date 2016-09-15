# "?" - Modifies the *,+, or {M,N}'d regexp that comes before to match as few times as possible.


import re

string1 = "Hello, world."
if re.search(r"l.?o", string1):
	print "The non-greedy match with 'l' followed by\n" +\
		"one or more characters is 'llo' rather than\n" +\
		"'llo wo'." 
