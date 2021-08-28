# 시간복잡도 O(N)

import sys
sys.stdin = open('input.txt')

N = int(input())

data = list(map(int, sys.stdin.readline().split()))
data.insert(0,0)
longer = [0] * (N + 1)
longer[1] = 1
shorter = [0] * (N + 1)
shorter[1] = 1
res = 0

for i in range(2, N + 1):
    if data[i] > data[i - 1]:
        longer[i] = longer[i - 1] + 1
        shorter[i] = 1
    elif data[i] < data[i - 1]:
        shorter[i] = shorter[i - 1] + 1
        longer[i] = 1
    else:
        longer[i] = longer[i - 1] + 1
        shorter[i] = shorter[i - 1] + 1

for m in range(1,len(longer)):
    if longer[m] > res:
        res = longer[m]
for n in range(1,len(shorter)):
    if shorter[n] > res:
        res = shorter[n]
print(res)