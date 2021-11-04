n = int(input())

for i in range(n):
    x, y = map(float, input().split())
    bpm = 60 * x / y
    val = 60 / y
    print("{:.4f} {:.4f} {:.4f}".format(bpm - val, bpm, bpm + val))
