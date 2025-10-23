## Code 49. Demonstrate Replace of every white-space character with "-"
import re

txt = "Hello guy's, I'm Rashid"
x = re.sub("\s", "-", txt)

print (x)
