import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    i = 1
    j = 1
    cnt = 1
    res = 0
    max_cnt = 0
    while i != M or j != N:
        if i == M and j < N:
            i = 1
            j += 1
            cnt += 1
            if i == x and j == y:
                res = cnt
                break
            continue
        if i < M and j == N:
            i += 1
            j = 1
            cnt += 1
            if i == x and j == y:
                res = cnt
                break
            continue
        if i < M and j < N:
            i += 1
            j += 1
            cnt += 1
            if i == M - 1 and j == N - 1:
                max_cnt = cnt
            if i == x and j == y:
                res = cnt
                break
    if max_cnt:
        print(-1)
    else:
        print(res)




