import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
M = int(sys.stdin.readline())
T = sys.stdin.readline().rstrip()

dp_left, dp_right = [0] * N, [0] * N

for i in range(N):
    for j in range(M):
        if i + j >= N:
            break
        if S[i + j] != T[j]:
            break
        dp_left[i] = j + 1

for i in range(N - 1, -1, -1):
    for j in range(M):
        if i - j < 0:
            break
        if S[i - j] != T[M - 1 - j]:
            break
        dp_right[i] = j + 1

flag = False

for i in range(N):
    for j in range(i, N):
        if (j - i + 1 < M):
            continue
        if dp_left[i] + dp_right[j] >= M:
            flag = True

if flag:
    print('YES')
else:
    print('NO')
