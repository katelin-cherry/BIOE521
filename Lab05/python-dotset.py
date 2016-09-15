# "[...]" Denotes a set of possible character matches
import re

string1= "Hello, world."

if re.search(r"[aeiou]+",string1):
	print string1 + " contains one or more vowels."
