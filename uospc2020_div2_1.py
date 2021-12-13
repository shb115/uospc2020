import sys

m = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

ans = (m // (a + b)) * a

if m % (a + b) > a:
    ans = ans + a
else:
    ans = ans + (m % (a + b))

print(ans)
