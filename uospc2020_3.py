import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

l = []

for i in range(n):
    if s[i] == '0':
        l.append(i)

leng = len(l)

if leng % 2 == 1:
    print(-1)
else:
    ans = 0

    for i in range(leng // 2):
        ans = ans + l[2 * i + 1] - l[2 * i]

    print(ans)
