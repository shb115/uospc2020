import sys

N = int(sys.stdin.readline())
x, y, w, h = map(int, sys.stdin.readline().split())

xmin, xmax, ymin, ymax = x - w, x + w, y - h, y + h

for _ in range(N - 1):
    x, y, w, h = map(int, sys.stdin.readline().split())

    xmin, xmax, ymin, ymax = max(xmin, x - w), min(xmax, x + w), max(ymin, y - h), min(ymax, y + h)

if xmin > xmax or ymin > ymax:
    print('impossible')
else:
    print(xmin, ymin)
