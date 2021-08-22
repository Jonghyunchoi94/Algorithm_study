# 8.16 - 8.22 homework

★ **8.22 18:00까지 제출**

## 1. 음양 더하기 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
        
    return answer
```



## 2. 약수의 개수와 덧셈 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j ==0:
                cnt += 1
        if cnt % 2:
            answer -= i
        else:
            answer += i
    return answer
```



## 3. 괄호 회전하기 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
open_bracket = '([{'
close_bracket = ')]}'

def right_check(data):
    stack = []
    for i in data:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            if (len(stack) == 0) or (len(stack) > 0 and stack.pop() != open_bracket[close_bracket.find(i)]):
                stack.append(i)
                break

    if len(stack):
        return False
    else:
        return True

def solution(s):
    answer = 0
    data_str = list(s)
    for i in range(len(s)):
        data_str.append(data_str.pop(0))
        if right_check(data_str):
            answer += 1
    return answer
```



## 4. 재귀호출과 완전 탐색 복습 (8.2 과제)

[소풍](https://algospot.com/judge/problem/read/PICNIC)   문제 주제와 맞게 풀어 복습해 보시오.

```python
# 완전탐색 방법 모색 실패 DFS 이용

import sys
sys.stdin = open('input.txt')

C = int(input())

def dfs(start,remain):
    if remain == 0:
        return 1
    cnt = 0
    for i in range(start,n):
        if not visited[i]:
            for j in range(i+1,n):
                if not visited[j] and G[i][j]:
                    visited[i] = visited[j] = 1
                    cnt += dfs(i, remain-2)
                    visited[i] = visited[j] = 0
    return cnt


for _ in range(C):
    n, m = map(int, input().split())
    G = [[0]*(n) for _ in range(n)]
    visited = [0]*n
    friend_data = list(map(int, input().split()))
    for i in range(m):
        G[friend_data[i * 2]][friend_data[i * 2 + 1]] = 1
        G[friend_data[i * 2 + 1]][friend_data[i * 2]] = 1
    print(dfs(0,n))
```



## 5. 재귀호출과 완전 탐색 복습 (8.2 과제)

[게임판 덮기](https://algospot.com/judge/problem/read/BOARDCOVER) 문제 주제와 맞게 풀어 복습해 보시오.

```python
import sys
sys.stdin = open('input.txt')

C = int(input())


move_index = [[(0,0),(0,1),(1,0)], [(0,0),(0,1),(1,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(1,-1)]]

def complete() :
    for x in range(H) :
        for y in range(W) :
            if data[x][y] == '.' :
                return x,y

    return -1,-1

def checkBlock(x,y,num) :

    for dx,dy in move_index[num] :

        nx = x+dx
        ny = y+dy

        if not (0 <= nx < H and 0 <= ny < W) :
            return False

        if data[nx][ny] == '#' :
            return False

    return True

def fillBlock(x,y,num) :

    for dx,dy in move_index[num] :
        nx = x+dx
        ny = y+dy
        data[nx][ny] = '#'

def removeBlock(x,y,num) :

    for dx, dy in move_index[num]:
        nx = x + dx
        ny = y + dy
        data[nx][ny] = '.'

def countBlock() :

    x,y = complete()

    if  x == -1 and y == -1 :
        return 1

    res = 0

    for m in range(len(move_index)) :
        if checkBlock(x,y,m) :
            fillBlock(x,y,m)
            res += countBlock()
            removeBlock(x,y,m)

    return res

for _ in range(C):
    H, W = map(int, input().split())
    data = [list(input()) for _ in range(H)]
    
    cnt = 0
    for i in range(H):
        for j in range(W):
            if data[i][j] == '.':
                cnt += 1
    if cnt % 3 == 0:
        print(countBlock())

    else:
        print(0)
```

