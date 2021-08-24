import sys
sys.stdin = open('input.txt')
# pypy3 통과 // python 53점
N = int(input())

map_data = [[0]*1001 for _ in range(1001)]

pos = []
for num in range(1, N + 1):
    left_r, left_c, right_r, right_c = map(int, input().split())
    pos.append(left_r)
    pos.append(left_r + right_r - 1)
    pos.append(left_c)
    pos.append(left_c + right_c - 1)
    for i in range(left_r, left_r + right_r):
        for j in range(left_c, left_c + right_c):
            map_data[i][j] = num

max_grid = max(pos)
min_grid = min(pos)

for n in range(1, N + 1):
    cnt = 0
    for i in range(min_grid, max_grid + 1):
        for j in range(min_grid, max_grid + 1):
            if map_data[i][j] == n:
                cnt += 1
    print(cnt)


