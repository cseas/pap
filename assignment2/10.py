import re

f = open("regex.txt", "r")
content = f.readlines()

# s = 'A message from cs@uni.edu to is@uni.edu'

for i in range(len(content)):
    if re.findall('[\w\.]+@[\w\.]+', content[i]):
        print(content[i], end='')