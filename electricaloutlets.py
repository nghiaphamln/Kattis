n = int(input())

for i in range(n):
    array = input().split()
    array = [(int(i)) for i in array][1:]
    r = 0
    for j in array:
        r += j - 1
    print(r + 1)
