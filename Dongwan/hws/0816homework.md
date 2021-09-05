# 8.16 - 8.22 homework

★ **8.22 18:00까지 제출**

## 1. 음양 더하기 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]: answer += absolutes[i] # True인 경우
        else: answer -= absolutes[i] # False인 경우
    return answer
```



## 2. 약수의 개수와 덧셈 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
# 방법1.
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        cnt = 1 # 자기자신
        for i in range(1, num): # 1 ~ num-1
            if num % i == 0: # 약수인 경우
                cnt += 1
        if cnt % 2: # cnt가 홀수인 경우
            answer -= num
        else: # 짝수인 경우
            answer += num
    return answer

# 방법2.
def solution(left, right):
    answer = 0
    for num in range(left, right+1): # left~right
        if int(num**0.5) == num**0.5: # 제곱수이면 약수가 홀수개
            answer -= num
        else: # 제곱수가 아니면 약수가 짝수개
            answer += num
    return answer

```



## 3. 괄호 회전하기 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
def solution(s):
    answer = 0
    pair = {')': '(', '}': '{', ']': '['} # 짝 지어 놓기
    s_list = list(s)
    
    for i in range(len(s)):
        s_list.append(s_list.pop(0)) # 한 칸씩 움직이기
        stack = []
        for i in s_list:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                if len(stack) == 0 or pair[i] != stack.pop(): # pop을 할 수 없고, 나온 값이 pair가 아닌 경우
                    break
        else: # for문이 정상적을 실행된 경우
            if len(stack) == 0: # stack이 0인 경우(남아 있으면 올바른 괄호 문자열이 아님)
                answer += 1
    return answer
```



## 4. 재귀호출과 완전 탐색 복습 (8.2 과제)

[소풍](https://algospot.com/judge/problem/read/PICNIC)   문제 주제와 맞게 풀어 복습해 보시오.

```python
def makepair(idx, team):
    global result
    if len(team) == N:  # team이 친구 수만큼 됐을 때 base case
        result += 1
        return
    
    for i in range(idx, N):  # 인원 수만큼 반복
        if i not in team:  # 해당 인원이 team에 없어야 함
            team.append(i)
            for pair in friend[i]:  # 해당 인원의 친구 반복
                if pair not in team:  # 해당 인원의 친구가 team에 없어야 함
                    team.append(pair)
                    makepair(i+1, team)
                    team.pop()  # 재귀 돌고 나왔으므로 다른 경우의 수를 위해 해당 인원의 친구 pop
            team.pop()  # 마찬가지로 재귀를 돌고 나온 것이므로 다른 경우의 수를 위해 해당 인원 pop

C = int(input())
for i in range(C):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    friend = [[] for _ in range(N)]
    result = 0

    for i in range(M):  # 인접리스트 생성
        friend[arr[i*2]].append(arr[i*2+1])

    makepair(0, [])
    print(result)
```



## 5. 재귀호출과 완전 탐색 복습 (8.2 과제)

[게임판 덮기](https://algospot.com/judge/problem/read/BOARDCOVER) 문제 주제와 맞게 풀어 복습해 보시오.

```python
# 방법1. 성공한 코드

def findpoint():  # 첫 시작지점을 찾는 함수
    for i in range(H):
        for j in range(W):
            if board[i][j] == '.':
                return i, j
    return -1, -1  # 블럭을 다 채운 경우

def ispossible(x, y, L):  # 블럭이 들어갈 수 있는지 점검하는 함수
    for dx, dy in move[L]:
        nx = x + dx
        ny = y + dy
        if not (0<=nx<H and 0<=ny<W):  # 범위 이외
            return False
        if board[nx][ny] == '#':  # 블럭이 들어갈 수 없음
            return False
    return True  # 블럭이 들어갈 수 있는 경우

def change(x, y, L, delta):  # 값을 바꾸는 함수
    for dx, dy in move[L]:
        nx = x + dx
        ny = y + dy
        board[nx][ny] = delta  # 지정한 값으로 변환

def boardcover():
    x, y = findpoint()
    
    if x == -1 and y == -1:  # 블럭을 다 채운 경우
        return 1
    
    result = 0  # 시작값 0
    for L in range(4):  # 방향 순환
        if ispossible(x, y, L):  # 가능한 경우
            change(x, y, L, '#')  # 블럭 채우기
            result += boardcover()
            change(x, y, L, '.')  # 블럭 치우기
    return result


move = [[(0,0),(1,0),(0,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(1,-1)], [(0,0),(0,1),(1,1)]]  # 왼쪽 맨위부터 실행하므로 4가지임(16가지가 아님)
C = int(input())
for _ in range(C):
    H, W = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(H)]

    print(boardcover())
```

```python
# 방법2. 실패한 코드

def boardcover(idx, board):
    global result
    if len(board) == len(blank):
        result += 1
        return

    for i in range(idx, len(blank)):
        x, y = blank[i][0], blank[i][1]
        if (x, y) not in board:
            for L in move:
                temp = {(x, y)}
                for dx, dy in L:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in blank and (nx,ny) not in board:
                        temp.add((nx, ny))
                    else:
                        break
                else:
                    board.update(temp)
                    boardcover(0, board)
                    board = board.difference(temp)

move = [[(1,0),(0,1)], [(1,0),(1,1)], [(1,0),(1,-1)], [(0,1),(1,1)]]
C = int(input())
for _ in range(C):
    H, W = map(int, input().split())
    game_map = [list(input().rstrip()) for _ in range(H)]
    result = 0

    blank = [(i, j) for i in range(H) for j in range(W) if game_map[i][j] == '.']
    boardcover(0, set())
    print(result)
```

