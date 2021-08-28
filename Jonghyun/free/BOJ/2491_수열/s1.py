import sys
sys.stdin = open('input.txt')

# 시간 초과 발생
N = int(input())

data = list(map(int, sys.stdin.readline().split()))
data.insert(0,0)
longer = [0] * (N + 1)
longer[1] = 1
shorter = [0] * (N + 1)
shorter[1] = 1
res = 0
for i in range(2, N + 1):
    min_val = 0
    max_val = 0
    for j in range(i-1, 0, -1):
        if data[i] >= data[j] and longer[j] >= max_val:
            max_val = longer[j]
        if data[i] <= data[j] and shorter[j] >= min_val:
            min_val = shorter[j]
    longer[i] = max_val + 1
    shorter[i] = min_val + 1

    if longer[i] > res:
        res = longer[i]
    if shorter[i] > res:
        res = shorter[i]

print(res)


