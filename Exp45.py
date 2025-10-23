## Code 45. Ddemonstrate  Regular expression search function
import re

txt = "Hello guy's, I'm Rashid"
x = re.search("guy's", txt)

if x:
    print("YES! Matched")
else:
    print("No match")
