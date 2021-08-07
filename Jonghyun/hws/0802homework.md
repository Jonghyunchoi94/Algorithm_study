# 8.2 - 8.8 homework

★**8.8 18:00까지 제출**

## 1. 그룹 단어 체커 (BOJ 1316번 )

```python
N = int(input())
cnt = 0
for _ in range(N):
    words = input()
    strings = ''
    for word in words:
        if (word not in strings) or (strings[-1] == word):
            strings += word
        
    if strings == words:
        cnt += 1
print(cnt)
```



## 2. 덩치 (BOJ 7568번)

```python
N = int(input())
order_list = []
for _ in range(N):
    x,y = list(map(int,input().split()))
    order_list.append((x,y))

for i in range(len(order_list)):
    ord = 1
    max_h = order_list[i][0]
    max_w = order_list[i][1]

    for j in range(len(order_list)):
        if (order_list[j][0] > max_h) and (order_list[j][1] > max_w):
            ord += 1
    print(ord, end = ' ')
```



## 3. 퇴사 (BOJ 14501번)

```python
def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)

n=int(input())
T=list()
P=list()
for i in range(n):
    a, b=map(int, input().split())
    T.append(a)
    P.append(b)
res=-2147000000
T.insert(0, 0)
P.insert(0, 0)
DFS(1, 0)
print(res)
```



## 4. 스타트와 링크 (BOJ 14889번)

```python
import sys
from itertools import combinations

N = int(input())

combi = list(combinations(range(1,N+1),N//2))
skills = [list(map(int,input().split())) for _ in range(N)]
members = [i for i in range(1,N+1)]

total_skills = sum([skills[i][j] for i in range(len(skills)) for j in range(len(skills[i])) ])


min_gap = sys.maxsize

for i in range(len(combi)//2):
    team = combi[i]
    stat_1 = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_1 += skills[member-1][k-1]
    
    team = combi[-i-1]
    stat_2 = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_2 += skills[member-1][k-1]
    

    min_gap = min(min_gap, abs(stat_1-stat_2))

print(min_gap)
```



## 5. 내적 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i] 
    return answer
```



## 6. 3진법 뒤집기 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
def solution(n):
    answer = ''
    while n > 0 :
        answer += str(n%3)
        n //= 3
    answer = answer[::-1]
    res = 0
    multi = 1
    for i in answer:
        res += (multi*int(i))
        multi *= 3 
```



## 7. 삼각 달팽이 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
def solution(n):
    answer = [[0]*n for _ in range(n)]
    move = [[1,0],[0,1],[-1,-1]]
    num = 0
    x = -1
    y = 0
    m = n
    move_index = 0
    
    while m > 0:
        cnt_list = []
        while len(cnt_list) < m:
            num += 1
            answer[x+move[move_index][0]][y+move[move_index][1]] = num
            cnt_list.append(num)
            
            x = x+move[move_index][0]
            y = y+move[move_index][1]
        if move_index == 2:
            move_index = 0
        else:
            move_index += 1
        m -= 1
    res = []
    for i in range(n):
        for j in range(n):
            if answer[i][j]!=0:
                res.append(answer[i][j])
               
    return res
```



## 8. 재귀 호출과 완전 탐색에 대해 탐구하고 설명하시오

```bash
흔히 무식하게 푼다에서 유래된 브루스 포스는 가능한 경우의 수를 일일이 나열하면서 답을 찾는 방법을 말합니다. 이렇게 가능한 방법을 전부 만들어 보는 알고리즘을 일컬어 완전 탐색이라고 부릅니다. 완전 탐색은 속도가 빠른 컴퓨터의 장점을 가장 잘 이용하는 방법입니다. 완전 탐색이 중요한 이유는 더 빠른 알고리즘의 기반이 되기 때문입니다. 보통 더 좋은 알고리즘을 구분하는 좋은 기준이 되는 알고리즘이 바로 완전 탐색 알고리즘입니다. 

컴퓨터가 수행하는 많은 작업들은 대개 작은 조각들로 나누어 볼 수 있습니다. 들여다보는 범위가 작아지면 작아질수록 각 조각들의 형태가 유사해지는 작업들을 많이 볼 수 있습니다. 완전히 같은 코드를 반복해 실행하는 작업을 할 때 유용하게 사용되는 개념이 재귀 호출입니다. 재귀 함수란, 자신이 수행할 작업을 유사한 형태의 여러 조각으로 쪼갠 뒤 그 중 한 조각을 수행하고, 나머지를 자기 자신을 호출해 실행하는 함수를 가리킵니다. 재귀 함수는 '더 이상 쪼개지지 않는' 최소한의 작업(base case)에 도달했을 때 답을 곧장 반환하는 조건문을 반드시 포함시켜야 합니다.

```

```python
# 재귀 함수 예시
def recursiveSum(n):
    if n==1:
        return 1
    return n + recursiveSum(n-1)
```



## 9. 보글게임

[보글게임 문제](https://algospot.com/judge/problem/read/BOGGLE)     :  이 문제는 다른 방법 말고 완전 탐색으로 푸시오 !

```python
C = int(input())

word_map = [list(input()) for _ in range(5)]

N = int(input())

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def hasWord(y,x,word):
    if (x not in range(N)) or (y not in range(N)):
        return False
    
    if word_map[y][x] != word[0]:
        return False

    if len(word)==1:
        return True
    
    for direct in range(8):
        next_y = y + dy[direct]
        next_x = x + dx[direct]

        if hasWord(next_y,next_x,word[1:]):
            return True
    return False
    
def hasWordall(word):
    start_point = []
    for y_index, row in enumerate(word_map):
        for x_index, alphabet in enumerate(row):
            if alphabet ==word[0]:
                start_point.append((y_index,x_index))
    for y,x, in start_point:
        output = hasWord(y,x,word)
        if output:
            return "YES"
    else:
        return "NO"

for _ in range(N):
    word = input()
    print(word, hasWordall(word))
```









