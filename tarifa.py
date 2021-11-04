x = int(input())
n = int(input())
result = x

for i in range(n):
    result = result + (x - int(input()))

print(result)
