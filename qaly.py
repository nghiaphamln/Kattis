n = int(input())
result = 0

for i in range(n):
    q, y = map(float, input().split())
    result = result + (q * y)

print(format(result, ".3f"))
