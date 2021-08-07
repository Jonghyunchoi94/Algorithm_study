# 8.2 - 8.8 homework

★**8.8 18:00까지 제출**

## 1. 그룹 단어 체커 (BOJ 1316번 )

```python
import sys

input = sys.stdin.readline
N = int(input())
result = 0

for _ in range(N):
    cnt = [0] * 26 # 알파벳 등장 횟수가 들어갈 공간
    alphabets = input().rstrip() # rstrip() 안하면 sys.stdin.readline에서는 빈 공백 하나 들어가서 인덱스 골치 아픔
    print(alphabets, len(alphabets))
    cnt[ord(alphabets[0])-97] += 1 # 첫 번째 인자가 for문에서 안 돌기 때문에 여기서 횟수 기록(아스키 코드 이용 // 소문자만 들어옴)
    
    for i in range(1, len(alphabets)): # 비교를 위해 범위는 1부터 시작
        if alphabets[i-1] != alphabets[i] and cnt[ord(alphabets[i])-97] != 0: # 이전 단어와 같지 않고, cnt 값이 1이 아닐 경우
            break
        cnt[ord(alphabets[i])-97] += 1 # 횟수 기록
    else: # break 안 걸린 경우
        result += 1 # 결과 +1

print(result)
```



## 2. 덩치 (BOJ 7568번)

```python
N = int(input())
people_size = [[] for _ in range(N)] # 사이즈 리스트 초기화
result = [0] * N # 등수 결과 리스트 초기화

for n in range(N): # 사이즈 입력 받기
    people_size[n] = list(map(int, input().split()))

for i in range(N):
    cnt = 1 # 등수는 1등부터 시작
    for j in range(N):
        if people_size[i][0] < people_size[j][0] and people_size[i][1] < people_size[j][1]: # 키, 몸무게 모두 작은 경우
            cnt += 1 # 등수 +1
    result[i] = cnt # 등수 결과 저장

print(*result)
```



## 3. 퇴사 (BOJ 14501번)

```python
import sys

input = sys.stdin.readline

N = int(input())
times = [0] * (N + 1) # 소요 시간을 저장할 공간
pays = [0] * (N + 1) # 급여를 저장할 공간
my_pay = [0] * (N + 1) # 내가 받을 수 있는 금액을 저장할 공간(인덱스는 일자를 의미)

for i in range(1, N + 1):
    times[i], pays[i] = list(map(int, input().split()))
    
for i in range(1, N + 1):
    if (times[i] + i) <= (N + 1): # 기한 내에 상담을 끝낼 수 있는 경우
        my_pay[times[i] + i - 1] = max(my_pay[times[i] + i - 1], max(my_pay[:i]) + pays[i]) # max(상담이 끝난 날의 급여, 현재 일까지 가장 큰 급여 + 오늘 상담을 시작하면 받는 금액)

print(max(my_pay))
```



## 4. 스타트와 링크 (BOJ 14889번)

```python
def best_match(A_team):
    A_total = 0 # A팀의 능력 합계
    B_total = 0 # B팀의 능력 합계

    B_team = list(set(list(range(N))) - set(A_team)) # B팀의 선수 구하기(filter 이용한 것이 더 빠를 것 같음)

    for i in A_team: # A팀 능력 합계 구하기
        for j in A_team:
            if i != j: # 자기자신이 아닌 경우
                A_total += team_map[i][j]
    
    for i in B_team: # B팀 능력 합계 구하기
        for j in B_team:
            if i != j: # 자기자신이 아닌 경우
                B_total += team_map[i][j]
    
    return abs(A_total - B_total) # 팀 능력치 차이의 절대값 반환


def dfs(idx, team):
    global best_score # 계속 변경해야 하는 값이므로 전역 변수 선언
    if idx == N//2: # idx가 N의 절반이 된 경우(한 팀만 구하면 되므로)
        value = best_match(team) # best_match 함수는 어차피 실행되어야 하므로 2번 시행 안되게 미리 값 받기
        if best_score > value: # 최적값보다 더 작은 경우
            best_score = value # 해당 값을 최적값으로 저장
            return # 불필요한 추가 연산이 안되도록 종료 시킴
    
    for i in range(max(team) + 1, N): # 범위 중 max(team) + 1 중요(해당 팀의 중복 선수 방지, 중복 팀 방지)
       team.append(i) # 팀에 i선수 추가
       dfs(idx+1, team) # 다음 dfs 진행(백트래킹)
       team.remove(i) # dfs 다 돌고오면, i선수 제외(아니면 계속 선수 누적됨)

import sys

input = sys.stdin.readline
N = int(input())
star_team = [0] # start팀 지정(0을 포함한 것은 미리 포함되어 있어도 결과에 상관 없고, 시간 단축시킬 수 있기 때문)
team_map = [[] for _ in range(N)] # team_map 초기화
best_score = sys.maxsize # 결과값 최대값으로 초기화

for i in range(N):
    team_map[i] = list(map(int, input().split()))

dfs(1, star_team)
print(best_score)
```



## 5. 내적 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
def solution(a, b):
    result = 0
        
    for i in range(len(a)):
        result += a[i] * b[i]
    
    return result
```



## 6. 3진법 뒤집기 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
def solution(n):
    change = '' # 3진법 변환을 저장할 변수
    result = 0 # 결과를 저장할 변수

    while n > 0: # n이 0보다 클 때, 반복
        change += str(n % 3) # 나머지를 저장(거꾸로 저장됨 -> 다시 거꾸로 변환 필요 X)
        n //= 3 # 몫만 저장
    
    for idx, value in enumerate(list(change)[::-1]):
        if int(value): # value 값이 True인 경우
            result += int(value) * (3**idx) # 10진수로 변환
        
    return result
```



## 7. 삼각 달팽이 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
# 방법1(내 풀이)
def solution(n):
    result = [[0] * i for i in range(1, n+1)]

    direc = 0 # 3으로 나눴을 때, 나머지에 따른 방향(0: 아래, 1: 오른쪽, 2: 대각선)
    state = 1 # 들어갈 값(1 ~ n(n+1))

    while direc < n: # 방향의 총 수는 n과 같음
        if direc % 3 == 0: # 아래인 경우
            for i in range(n-direc): # 횟수는 n부터 -1씩 줄어들게 됨(이를 n-direc으로 구현)
                result[i + 2*(direc//3)][direc//3] = state
                state += 1
        elif direc % 3 == 1: # 오른쪽인 경우
            for i in range(n-direc):
                result[n - 1 - direc//3][i + direc//3 + 1] = state
                state += 1
        else: # 대각선인 경우
            for i in range(n-direc):
                result[n - 2 - i - direc//3][n - 2 - i - 2*(direc//3)] = state
                state += 1

        direc += 1

    return sum(result, [])

# 방법2(다른 사람 풀이 참고)
def solution(n):
    result = [[0] * i for i in range(1, n+1)]

    [row, col, cnt] = [-1, 0, 1] # 행, 열, 값 초기화

    for i in range(n): # n까지
        for j in range(n-i): # n-i까지(방향마다 하나씩 줄어듬)
            if i % 3 == 0: # 아래인 경우
                row += 1 # 행 +1(그래서 초기값 -1)
            
            elif i % 3 == 1: # 오른쪽인 경우
                col += 1 # 열 +1(처음 열 값은 1이어야 함. 그래서 초기값 0)
            
            else: # 대각선인 경우
                row -= 1 # 행 -1
                col -= 1 # 열 -1
            
            result[row][col] = cnt # 해당 행, 열에 값 입력
            cnt += 1 # 값 +1

    return sum(result, [])
```



## 8. 재귀 호출과 완전 탐색에 대해 탐구하고 설명하시오

```bash
재귀함수
재귀함수란 함수 내부에서 자기 자신을 다시 호출하여 실행되게 하는 것을 말한다. 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴해야 한다. 즉, 큰 문제를 해결하기 위해 작은 문제로 좁히고, 작은 문제의 해답을 이용하고, 이 작은 문제는 base case에 도달하여 재귀 함수가 끝나야 한다. 일반적으로 단순 for문 보다 속도가 느리지만, 로직을 만들기 쉬운 편이다.

완전 탐색
브루트 포스라고도 불리며, 말 그대로 모든 경우의 수를 다 계산하는 방식을 말한다. 제시된 문제에 부합하는 모든 조건을 고려하여 해답을 찾아내는 방식으로 직관적이고 구현이 쉽다는 장점이 있지만, 시간이 오래 걸리며 비효율적이다.
```



## 9. 보글게임

[보글게임 문제](https://algospot.com/judge/problem/read/BOGGLE)     :  이 문제는 다른 방법 말고 완전 탐색으로 푸시오 !

```python
# 재귀, 메모이제이션의 방법을 사용했습니다.
def boglebogle(idx, dx, dy):
    global confirm # 값을 변경해야 하므로 global 선언(False -> True)
    if idx == len(word) or confirm: # 찾는 단어 길이와 idx가 같거나 이미 답을 찾은 경우
        confirm = True # True로 변경
        return # 추가적인 계산을 막기 위한 return(반환의 의미는 아님 -> 여기서 반환해도 for문 안에 있는 경우가 있으므로 의미 X)

    for x, y in xy: # 이동 반복
        if bogle_map[dx + x][dy + y] == word[idx] and (dx+x, dy+y, idx) not in visited: # 해당 좌표 값이 찾는 글자이고, 방문하지 않은 경우
            visited.add((dx + x, dy + y, idx)) # 방문 기록을 남김(idx가 없으면 해당 좌표 다시 방문 못함 -> 반드시 idx가 같은 경우 같은 좌표를 방문 못하게 해야 함)
            boglebogle(idx+1, dx + x, dy + y) # 재귀(idx는 +1)

import sys

input = sys.stdin.readline
C = int(input())
xy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] # x, y가 움직일 공간(12시부터 시계 방향)

for i in range(C):
    bogle_map = [[0] * 7] + [[] for _ in range(5)] + [[0] * 7] # 테두리 0으로 만들어줌
    
    for i in range(1, 6): # 테두리가 있으므로 범위 주의
        bogle_map[i] = [0] + list(input().rstrip()) + [0] # 입력받는 값 양 끝에 0을 더해서 테두리 만듬

    N = int(input())

    for _ in range(N):
        confirm = False # 답을 찾았을 때, 불필요한 재귀들을 더 이상 안 돌게 하기 위한 변수(값 찾으면 True로 바꿈)
        word = input().rstrip() # sys.stdin.readline은 입력값 뒤에 '\n' 붙으므로 rstrip()으로 제거
        visited = set() # 방문했는지 점검하기 위한 집합(단, (x좌표, y좌표, idx)의 특이한 값을 사용// 단순 확인이므로 집합 사용)

        start_list = [(i, j) for i in range(7) for j in range(7) if bogle_map[i][j] == word[0]] # 첫 단어와 일치하는 좌표 확인(여기서도 범위는 5가 아닌 7)
        for i, j in start_list: # 해당 좌표 반복
            boglebogle(1, i, j) # 재귀 시작(입력할 때, idx(몇 번째 글자인지 확인할 변수)는 1로 함 -> 이미 첫 단어 찾았으므로)
            if confirm: # 답을 찾은 경우
                print(word, 'YES')
                break
        else: # 못 찾은 경우(for문이 정상적으로 반복 후)
            print(word, 'NO')
```









