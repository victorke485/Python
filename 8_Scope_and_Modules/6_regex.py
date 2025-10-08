# RegEx (regular Expression) is a sequance oc characters that forms a search pattern

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

