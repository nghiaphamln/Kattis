n = int(input())
array = input().split()
array = [(int(i)) for i in array]
r = 0
for j in array:
    r += j
print(r)
