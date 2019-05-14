f = open("a.txt", "r")

content = f.readlines()

for i in range(10):
    # end is used for avoiding print function's newlines
    print(content[i], end='')

for i in range(len(content) - 10, len(content)):
    print(content[i], end='')

f.close()