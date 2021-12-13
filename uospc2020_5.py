import sys

n, m, l = map(int, sys.stdin.readline().split())
covid = list(map(int, sys.stdin.readline().split()))
meet = [list(map(int, sys.stdin.readline().split())) for _ in range(l)]

meet.sort(key = lambda x:x[2], reverse = True)

is_covid = [False] * (m + 1)
for i in covid:
    is_covid[i] = True
    
stack = []
adj = [[] for _ in range(m + 1)]
for i in range(l):
    a, b, c = meet[i]
    stack.append([a, b])
    if i == l - 1 or meet[i + 1][2] != c:
        q = []
        visit = set()
        for a, b in stack:
            if is_covid[a]:
                q.append(a)
                visit.add(a)
            if is_covid[b]:
                q.append(b)
                visit.add(b)
            adj[a].append(b)
            adj[b].append(a)
        q = list(set(q))
        for a in q:
            for b in adj[a]:
                if b in visit:
                    continue
                visit.add(b)
                is_covid[b] = True
                q.append(b)
        for a, b in stack:
            adj[a] = []
            adj[b] = []
        stack = []

for i in range(1, m + 1):
    if is_covid[i]:
        print(i)
