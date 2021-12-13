import sys

W, H, N = map(int, sys.stdin.readline().split())
Map = [sys.stdin.readline() for _ in range(H)]

adj = [[0 for _ in range(W)] for __ in range(H)]
dp = [0] * (H + 1)
ans = []

for i in range(W):
    for j in range(H):
        if Map[j][i] != 'X':
            adj[j][i] = adj[j - 1][i] + 1           

for j in range(H):
    s = [[adj[j][0], 0]]
    for i in range(1, W):
        while s and adj[j][i] < s[-1][0]:
            h, w = s.pop()
            if s:
                w = i - s[-1][1] - 1
            else:
                w = i
            dp[h] = max(dp[h], w)
        s.append([adj[j][i], i])
    while s:
        h, w = s.pop()
        if s:
            w = W - s[-1][1] - 1
        else:
            w = W
        dp[h] = max(dp[h], w)

for i in range(N):
    a, c = map(int, sys.stdin.readline().split())
    if dp[c] >= a:
        ans.append(i + 1)

print(len(ans))
for i in ans:
    print(i, end = ' ')
