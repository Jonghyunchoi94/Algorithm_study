# 종이 자르기

import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split())

N = int(input())

res = []
for case in range(N):
    a1, a2 = map(int,input().split())
    res.append([a1,a2])

res.extend([[0,0],[1,0]])
sort_res = sorted(res, key= lambda x: (x[0],x[1]), reverse = True)
print(sort_res)
max_value_x = 0
max_value_y = 0
for i, j in sort_res:
    if i == 0:
        if max_value_x < C - j:
            max_value_x = C - j
        C = j
    elif i == 1:
        if max_value_y < R - j:
            max_value_y = R - j
        R = j
width = 0
if max_value_x == 0 and max_value_y == 0:
    width = R * C
elif max_value_x == 0:
    width = max_value_y * C
elif max_value_y == 0:
    width = max_value_x * R
else:
    width = max_value_x * max_value_y

print(width)
