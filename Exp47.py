## Code 47. Ddemonstrate Search for the first white space character in the string using Regular expression.
import re

txt = "Hello guy's, I'm Rashid"
x = re.search("\s", txt)

print("The first white space located at", x.start())
