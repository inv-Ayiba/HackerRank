import re

#alphanumeric regular expressions ... yeah
# '^[a-zA-Z0-9]+$'
# '(?P<user>\w+)^[a-zA-Z0-9]+$'

m = re.search(r'([a-zA-Z0-9])\1','..23345678910111213141516171820212223')

# m = re.search(r'([a-zA-Z0-9])\1','..13234563789')
# print(m.group(1))

try:
    print(m.group(1))
except(AttributeError):
    print(-1)

# print(m.group(1) if m else -1)


    