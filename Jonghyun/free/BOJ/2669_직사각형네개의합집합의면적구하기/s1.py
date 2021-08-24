import sys
sys.stdin = open('input.txt')

pos = {}
for _ in range(4):
    left_r, left_c, right_r, right_c = map(int, input().split())
    for i in range(left_r, right_r):
        for j in range(left_c, right_c):
            if (i, j) not in pos:
                pos[(i, j)] = 1
            else:
                pos[(i, j)] += 1

print(len(pos))
