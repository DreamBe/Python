import re

content = "aababbaxz abcabb abbbbabb1111"
pattern = re.compile("[ab]*abb")

print(pattern.findall(content))
