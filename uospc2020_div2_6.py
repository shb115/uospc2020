import sys
sys.setrecursionlimit(10000)

def dfs(p, t):
    child[p].sort()
    cur = t
    h = 0
    for h_i, c in child[p]:
        cur = cur + (h_i - h) * S[p]
        cur = dfs(c, cur)
        h = h_i
    cur = cur + (H[p] - h) * S[p]
    ans[p] = cur
    return cur

N = int(sys.stdin.readline())
S, H = [0] * N, [0] * N,

for i in range(N):
    S[i], H[i] = map(int, sys.stdin.readline().split())

ans = [0] * N
child = [[] for _ in range(N)]

adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, h = map(int, sys.stdin.readline().split())
    child[u - 1].append([h, v - 1])

dfs(0, 0)
for i in ans:
    print(i)
