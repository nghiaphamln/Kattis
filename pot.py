n = int(input())
result = 0

for i in range(n):
    element = input()
    result += int(element[:-1]) ** int(element[-1])

print(result)
