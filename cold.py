n = int(input())

array = [int(i) for i in input().split()]

count = 0

for i in array:
    if i < 0:
        count += 1

print(count)
