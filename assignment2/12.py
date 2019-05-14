from statistics import mean

N = int(input("No. of integers: "))
print("Enter integers:")

lst = []
for i in range(N):
    lst.append(int(input()))

print(lst)
print(mean(lst))