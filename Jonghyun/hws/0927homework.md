# 9.27 - 10.3 homework

★ **스터디 전까지 제출**

## 1. 요리사 (SWEA 4012)

```python
def dfs(num, s):
    if num == N // 2:
        res = visited[:]
        com_food.append(res)
        return

    for i in range(s, N):
        visited[num] = i
        dfs(num + 1, i + 1)

def combi(data):
    res = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            res += food[data[i]][data[j]]
            res += food[data[j]][data[i]]
    return res


T = int(input())

for case in range(T):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N // 2)
    com_food = []
    dfs(0, 0)
    ans = 987654321
    for k in range(len(com_food)//2):
        food_a = 0
        food_b = 0
        food_a += combi(com_food[k])
        food_b += combi(com_food[len(com_food) - 1 - k])
        if ans > abs(food_a - food_b):
            ans = abs(food_a - food_b)
    print('#{} {}'.format(case + 1, ans))
```

## 2. 보물상자 비밀번호 (SWEA 5658)

```python
T = int(input())

for case in range(T):
    N, K = map(int, input().split())
    password = list(input())
    rotate = len(password) // 4
    m = rotate
    set_data = set()
    while m > 0:
        for idx in range(0, len(password), rotate):
            set_data.add(''.join(password[idx: idx + rotate]))
        password.append(password.pop(0))
        m -= 1

    sorted_data = sorted(list(set_data), key = lambda x:int(x,16), reverse = True)
    print('#{} {}'.format(case + 1, int(sorted_data[K - 1], 16)))
```

## 3. 물놀이를 가자 (SWEA 10966)

```python
# 물에서 땅으로 (최적화 완료 !! )

from collections import deque

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for case in range(T):
    N, M = map(int, input().split())
    # 매우 중요한 insight
    # list(input()) 으로 할 시 runtime error !
    # input() 으로 할 시 통과 !

    data = [input() for _ in range(N)]
    less_visited = [[987654321] * M for _ in range(N)]
    q = deque()
    for r in range(N):
        for c in range(M):
            if data[r][c] == 'W':
                q.append([r, c])
                less_visited[r][c] = 0
    # 연산량을 줄이기 위해 불필요한 계산 줄이는 방법 !!
    while q:
        x, y = q.popleft()
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if 0 <= next_x < N and 0 <= next_y < M and data[next_x][next_y] == 'L' and less_visited[next_x][next_y] == 987654321:
                less_visited[next_x][next_y] = less_visited[x][y] + 1
                q.append([next_x, next_y])
    res = 0
    for i in less_visited:
        for j in i:
            res += j
    print('#{} {}'.format(case + 1, res))

```

## 4. 보호필름 (SWEA 2112)

```python
def inspect(film,K):
    for i in range(W):
        stack = 0
        for j in range(D-1):
            if film[j][i] == film[j+1][i]:
                stack += 1
            else :
                stack = 0
            if stack == K-1 :
                break
        if stack != K-1 :
            return False
    return True

def dfs(L,s,film):
    global ans
    if L >= answer:
        return
    if inspect(film,K):
        if L < ans:
            ans = L
        return
    if L == K:
        if L < ans:
            ans = L
        return
    else :
        for i in range(s,D):
            switched = []
            for j in range(W):
                if film[i][j] == 1:
                    film[i][j] = 0
                    switched.append(j)
            dfs(L+1, i+1, film)
            for j in switched:
                film[i][j] = 1

            switched = []
            for j in range(W):
                if film[i][j] == 0:
                    film[i][j] = 1
                    switched.append(j)
            dfs(L+1, i+1, film)
            for j in switched:
                film[i][j] = 0


T = int(input())
for case in range(T):

    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    ans = 987654321
    if K == 1:
        print('#{} {}'.format(case + 1, 0))
    else :
        dfs(0,0,films)
        print('#{} {}'.format(case + 1, ans))
```

## 5. 탈주범 검거 (SWEA 1953)

```python
import sys
sys.stdin = open('input.txt')

T = int(input())

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

hole = {
    1 : [0, 1, 2, 3],
    2 : [0, 2],
    3 : [1, 3],
    4 : [0, 1],
    5 : [1, 2],
    6 : [2, 3],
    7 : [0, 3],
}

direction = {
    0 : 2,
    1 : 3,
    2 : 0,
    3 : 1,
}

def dfs(r, c, time):
    if time == L:
        return

    for k in range(4):
        if k in hole[road[r][c]]:
            next_r = r + dr[k]
            next_c = c + dc[k]
            if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c] == 0 and road[next_r][next_c] and (direction[k] in hole[road[next_r][next_c]]):
                record.add((next_r, next_c))
                visited[r][c] = 1
                dfs(next_r, next_c, time + 1)
                visited[r][c] = 0
    return

for case in range(T):
    N, M, R, C, L = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    record = {(R, C)}
    dfs(R, C, 1)
    print('#{} {}'.format(case + 1, len(record)))
```





