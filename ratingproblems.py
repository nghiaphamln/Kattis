n, k = map(int, input().split())
min_result = -3 * (n - k)
max_result = 3 * (n - k)

for i in range(k):
    temp = int(input())
    min_result = min_result + temp
    max_result = max_result + temp

print("{} {}".format(min_result/n, max_result/n))
