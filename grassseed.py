c = float(input())
l = int(input())
r = float()
for i in range(l):
    w, h = map(float, input().split())
    r += (w * h) * c

print("{:.7f}".format(r))
