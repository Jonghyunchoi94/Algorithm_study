import sys
sys.stdin = open('input.txt')

dice = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

def stair(row_list, val):
    for i in range(len(row_list)):
        if row_list[i] == val:
            return row_list[dice[i]]
for i in range(6):
    for j in range(N):
        stair(data[j], data[j][i])


