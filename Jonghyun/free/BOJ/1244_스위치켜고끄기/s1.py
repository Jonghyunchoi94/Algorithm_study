# 스위치 켜고 끄기

import sys
sys.stdin = open('input.txt')

T = int(input())
switch = [0] + list(map(int,input().split()))

N = int(input())

def change(n):
    if n == 1:
        return 0
    elif n == 0:
        return 1

for case in range(N):
    sex, number = map(int, input().split())

    if sex == 1:
        for i in range(1, T + 1):
            if i % number == 0:
                switch[i] = change(switch[i])
    elif sex == 2:
        switch[number] = change(switch[number])
        for j in range(1, T//2 + 1 ):
            if (number + j <= T) and (number - j > 0) and (switch[number + j] == switch[number - j]):
                switch[number + j] = change(switch[number + j])
                switch[number - j] = change(switch[number - j])
            else:
                break
cnt = 0
ans = ''
for res in range(1, T + 1):
    ans += (str(switch[res]) + ' ')
    cnt += 1
    if cnt == 20:
        print(ans)
        ans = ''
        cnt = 0
if len(ans) != 0:
    print(ans)

