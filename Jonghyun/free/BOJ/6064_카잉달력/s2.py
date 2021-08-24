import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    year_M = [x for x in range(x, M * N + 1, M)]
    year_N = [y for y in range(y, M * N + 1, N)]

    res = 0
    for c in year_M:
        for d in year_N:
            if c < d:
                break
            if c == d:
                res = c
                break
        if res == c:
            print(res)
            break
    else:
        print(-1)


