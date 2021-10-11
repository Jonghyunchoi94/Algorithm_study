# 10.4 - 10.11 homework

★ **스터디 전까지 제출**

## 1. 특이한 자석 (SWEA 4013)

```python
'''
1번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 1점을 획득
2번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 2점을 획득
3번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 4점을 획득
4번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 8점을 획득

4개 자석의 자성 정보와 자석을 1칸씩 K번 회전시키려고 할 때,
K번 자석을 회전시킨 후 획득하는 점수의 총 합을 출력

자석의 개수는 4개이며, 각 자석은 8개의 날을 가지고 있다.
자석을 회전시키는 횟수 K( 1 ≤ K ≤ 20 )
하나의 자석이 1칸 회전될 때, 붙어 있는 자석은 서로 붙어 있는 날의 자성이 다를 경우에만 반대방향으로 1칸 회전

자석을 회전시키는 방향은 시계방향이 1, 반시계 방향이 -1

날의 자성은 N극이 0, S극이 1
각 자석의 날 자성정보는 빨간색 화살표 위치의 날부터 시계방향 순서대로
'''

def rotation_play(i):
    if i[0] == 1 and visited[i[0] -1] == 0:         # 첫번째, 방문안했으면
        visited[i[0] - 1] = 1                       # 방문체크
        if i[1] == 1:                               # 시계
            if visited[i[0]] == 1:                  # 2에서 넘어왔다면
                magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]   # 회전
            else:                                   # 1이 선택된거면
                if magnet[i[0] - 1][2] == magnet[i[0]][-2]:     # 같으면
                    magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]   # 회전
                else:                                           # 다르면
                    magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]   # 회전
                    rotation_play((2, -1))          # 2번도 회전(반대반향으로)
        else:                                       # 반시계
            if visited[i[0]] == 1:                  # 2에서 넘어왔다면
                magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
            else:                                   # 1이 선택된거면
                if magnet[i[0] - 1][2] == magnet[i[0]][-2]:
                    magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                else:
                    magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    rotation_play((2, 1))

    elif i[0] == 4 and visited[i[0] -1] == 0:       # 네번째, 방문안했으면
        visited[i[0] - 1] = 1
        if i[1] == 1:
            if visited[i[0]-2] == 1:
                magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
            else:
                if magnet[i[0] - 1][-2] == magnet[i[0] - 2][2]:
                    magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                else:
                    magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                    rotation_play((3, -1))
        else:
            if visited[i[0] - 2] == 1:
                magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
            else:
                if magnet[i[0] - 1][-2] == magnet[i[0] - 2][2]:
                    magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                else:
                    magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    rotation_play((3, 1))

    else:                                           # 두/세번째
        if visited[i[0] - 1] == 0:
            visited[i[0] - 1] = 1
            if i[1] == 1:
                if visited[i[0] - 2] == 1:          # 왼쪽에서 넘어왔다면
                    if magnet[i[0] - 1][2] == magnet[i[0]][-2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                    else:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0]+1, -1))
                elif visited[i[0]] == 1:        # 오른쪽에서 넘어왓따면
                    if magnet[i[0] - 1][-2] == magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                    else:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0]-1, -1))
                else:                           # 내가 시작이라면
                    if magnet[i[0] - 1][2] == magnet[i[0]][-2] and magnet[i[0] - 1][-2] == magnet[i[0] - 2][2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                    elif magnet[i[0] - 1][2] != magnet[i[0]][-2] and magnet[i[0] - 1][-2] == magnet[i[0] - 2][2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0] + 1, -1))
                    elif magnet[i[0] - 1][2] == magnet[i[0]][-2] and magnet[i[0] - 1][-2] != magnet[i[0] - 2][2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0] - 1, -1))
                    else:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0] + 1, -1))
                        rotation_play((i[0] - 1, -1))
            else:
                if visited[i[0] - 2] == 1:
                    if magnet[i[0] - 1][2] == magnet[i[0]][-2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    else:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]+1, 1))
                elif visited[i[0]] == 1:
                    if magnet[i[0] - 1][-2] == magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    else:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]-1, 1))
                else:
                    if magnet[i[0] - 1][2] == magnet[i[0]][-2] and magnet[i[0] - 1][-2] == magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    elif magnet[i[0] - 1][2] != magnet[i[0]][-2] and magnet[i[0] - 1][-2] == magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]+1, 1))
                    elif magnet[i[0] - 1][2] == magnet[i[0]][-2] and magnet[i[0] - 1][-2] != magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]-1, 1))
                    else:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]+1, 1))
                        rotation_play((i[0]-1, 1))

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K = int(input())                                                    # 회전 횟수
    magnet = [list(map(int, input().split())) for _ in range(4)]        # 자석 정보
    rotate = [tuple(map(int, input().split())) for _ in range(K)]       # [몇번 자석, 어느 방향] K(횟수)만큼 있음
    # print(magnet)
    # print(rotate)
    total_score = 0

    for r in rotate:
        visited = [0] * 4       # 방문 체크, 역으로 다시 안가게
        rotation_play(r)        # 자석번호(idx+1), 회전방향

    if magnet[0][0] == 1:       # 최종 계산
        total_score += 1
    if magnet[1][0] == 1:
        total_score += 2
    if magnet[2][0] == 1:
        total_score += 4
    if magnet[3][0] == 1:
        total_score += 8

    print('#{} {}'.format(tc, total_score))
    
```



## 2. 수영장 (SWEA 1952) [풀이강의 有]

```python
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    fee = list(map(int, input().split()))       # 1일, 1달 (같이 움직) / 3달 / 1년(마지막에 1번만 사용)
    plan = list(map(int, input().split()))
    # print(fee)
    # print(plan)

    dp = [0] * 13       # 1~12월, 0월은 1월부터 계산들어가면 있어야함 (전달 더하기니까)

    for i in range(12):     # 달력 돌면서
        if plan[i] == 0:
            dp[i+1] = dp[i]     # 0이면 비용이 그대로 진행
        else:
            if i < 2:           # 1, 2월까지는 3달비용 의미 없음
                dp[i+1] = dp[i] + min(plan[i] * fee[0], fee[1])     # 이전꺼 더하기 / 1일이랑 1달중에 최소비용

            else:
                dp[i+1] = min(dp[i] + plan[i] * fee[0], dp[i] + fee[1], dp[i-2] + fee[2])       # 1일, 1달, 3달 중 최소비용 (3달은 3달전꺼 더하기)

    print('#{} {}'.format(tc, min(dp[-1], fee[-1])))        # 마지막 1년은 최종 비용이랑 비교
    
```



## 3. 가능한 시험 점수 (SWEA 3752)

```python
# DP 힌트 얻고, DP 읽음
# 앞에서 했는데 도저히 안되서, 뒤로 하니까... 됨!

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    score_list = list(map(int, input().split()))

    dp = [0] * (sum(score_list) + 1)        # 0부터 최대까지

    dp[0] = 1                               # 0은 무조건 되니까 체크

    for i in score_list:                    # 0+2 / 2+3, 0+3 / 5+5, 3+5, 2+5, 0+5(중복)
        for j in range(len(dp)-1, -1, -1):
            if dp[j] == 1:
                dp[i+j] = 1

    print('#{} {}'.format(tc, sum(dp)))
    
```



## 4. 숫자 만들기 (SWEA 4008)

```python
'''
우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
게임 판에 적힌 숫자의 개수 N( 3 ≤ N ≤ 12 )
연산자 카드 개수의 총 합은 항상 N - 1
게임 판에 적힌 숫자는 1 이상 9 이하의 정수
수식을 완성할 때 각 연산자 카드를 모두 사용해야
숫자와 숫자 사이에는 연산자가 1 개만 들어가야
나눗셈을 계산 할 때 소수점 이하는 버린다.
입력으로 주어지는 숫자의 순서는 변경할 수 없다.
정답은 만들 수 있는 수식으로 얻은 결과값 중 최댓값과 최솟값의 차이
'''

import sys
sys.stdin = open('input.txt')

def DFS(idx, result):
    global max_num
    global min_num
    global new_result

    if idx == N-1:
        if max_num < result:
            max_num = result
        if min_num > result:
            min_num = result
            return

    for i in range(4):
        if operator_num[i] > 0:
            operator_num[i] -= 1
            if i == 0:
                new_result = result + number_list[idx+1]
            elif i == 1:
                new_result = result - number_list[idx+1]
            elif i == 2:
                new_result = result * number_list[idx+1]
            else:
                new_result = int(result / number_list[idx+1])   # int : 정수형으로 처냄
            DFS(idx+1, new_result)
            operator_num[i] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operator_num = list(map(int, input().split()))      # + - * /
    number_list = list(map(int, input().split()))       # 순서보장

    max_num = -987654321
    min_num = 987654321
    new_result = 0          # 계산값

    DFS(0, number_list[0])  # idx 시작, 첫값으로 시작

    print('#{} {}'.format(tc, max_num - min_num))
    
```



## 5. 벌꿀 채취 (SWEA 2115)

```python
'''
N*N 개의 벌통
각 칸의 숫자는 각각의 벌통에 있는 꿀의 양을 나타내며, 꿀의 양은 서로 다를 수 있다.

두 명의 일꾼
채취할 수 있는 벌통의 수 M, 가로로 연속되도록 M개의 벌통을 선택
단, 두 명의 일꾼이 선택한 벌통은 서로 겹치면 안 된다.

두 일꾼이 채취할 수 있는 꿀의 최대 양은 C (2개 합해서 C초과이면, max로 넣어줌)

이익은 넣어준거 각각 제곱의 합
최대이익 출력!

(3 ≤ N ≤ 10)
(1 ≤ M ≤ 5)
M은 반드시 N 이하
(10 ≤ C ≤ 30)
하나의 벌통에서 채취할 수 있는 꿀의 양은 1 이상 9 이하의 정수
하나의 벌통에서 일부분의 꿀만 채취할 수 없고, 벌통에 있는 모든 꿀을 한번에 채취
'''

def find_honey(m, n):       # m : M 채취가로 / n : 0이면 처음, 1이면 그다음, 2일때 종료
    global max_profit

    def find_max_comb(l, c):
        nonlocal profit

        sorted(l)
        for u in l:
            if sum(l) - u <= c:
                for s in l:
                    if s != u:
                        profit += s ** 2
                return
            else:
                continue

    if n == 2:
        profit = 0
        for i in stack:
            if sum(i) > C:      # 여기를 어떻게 할까
                find_max_comb(i, C)

            else:
                for j in i:
                    profit += j ** 2

        if profit > max_profit:
            max_profit = profit
            return
        else:
            return

    for i in range(N):
        for j in range(N-m+1):      # N-m+1 = 3 / 0,1,2까지만 범위 설정(가능한)

            if visited[i][j] == 0:

                if visited[i][j+m-1] == 0:

                    for k in range(m):
                        visited[i][j+k] = 1
                        stack[n].append(honey[i][j + k])

                    find_honey(m, n+1)

                    for k in range(m):
                        visited[i][j+k] = 0
                        stack[n].pop()

                else:
                    break
            else:
                break

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())     # N : 전체가로 / M : 채취가로 / C :최대양

    honey = [list(map(int, input().split())) for _ in range(N)]
    # print(honey)
    visited = [[0] * N for _ in range(N)]
    max_profit = 0

    stack = [[], []]

    find_honey(M, 0)

    print('#{} {}'.format(tc, max_profit))

```

