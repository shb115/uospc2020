import sys

S, T = sys.stdin.readline().split()

arr_S, arr_T = [], []

for i in range(2, 11):
    try:
        arr_S.append(int(S, i))
    except:
        pass
    try:
        arr_T.append(int(T, i))
    except:
        pass

ans = 0

for i in range(len(arr_S)):
    for j in range(len(arr_T)):
        if arr_S[i] == arr_T[j]:
            ans = ans + 1

print(ans)
