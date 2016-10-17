import re

content = "aababbaxz abcabb abbbbabb"
pattern = re.compile("[ab]*abb")

print(pattern.findall(content))
