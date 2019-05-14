try:
    f1 = open("FROM.txt", "r")
except FileNotFoundError:
    print("Specified file not found")
    exit()

f2 = open("VOWELTEXT.txt", "w")

content = f1.readlines()

vowels = ('a', 'e', 'i', 'o', 'u')

for i in range(len(content)):
    if(content[i].lower().startswith(vowels)):
        f2.write(content[i])

f1.close()
f2.close()