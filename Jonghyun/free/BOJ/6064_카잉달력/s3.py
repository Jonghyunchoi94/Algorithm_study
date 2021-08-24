import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    flag = True
    while x <= M * N:
        if x % N == y % N:
            print(x)
            flag = False
            break
        x += M
    if flag:
        print(-1)