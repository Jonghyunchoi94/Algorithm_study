# 9.27 - 10.3 homework

★ **스터디 전까지 제출**

## 1. 요리사 (SWEA 4012)

```python
def cal(a):  # 두 요리의 차를 계산하는 함수
    b = list(set([i for i in range(N)]) - set(a))

    a_s = b_s = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            a_s += (A[a[i]][a[j]] + A[a[j]][a[i]])  # a 계산
            b_s += (A[b[i]][b[j]] + A[b[j]][b[i]])  # b 계산
    return abs(a_s-b_s)


def dfs(foods):
    global ans
    if len(foods) == N // 2:  # base case
        ans = min(ans, cal(foods))
        return
    
    for i in range(max(foods)+1, N):
        foods.append(i)
        dfs(foods)  # 백트래킹
        foods.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**7  # 문제상 최댓값 고려

    dfs([0])  # 0은 미리 포함되어도 결과에는 상관 없음(시간 단축)
    print('#{0} {1}'.format(tc, ans))
```

## 2. 보물상자 비밀번호 (SWEA 5658)

```python
from collections import deque


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = deque(list(input()))

    ans = set()
    for _ in range(N):
        for i in range(0, N, N//4):
            t = '0x'  # 16진수 변환을 위해 지정
            for j in range(N//4):
                t += A[i+j]
            ans.add(int(t, 16))  # 16진수 문자열 => 10진수 변환 후 저장
        A.appendleft(A.pop())  # 회전

    print('#{0} {1}'.format(tc, sorted(list(ans), reverse=True)[K-1]))
```

## 3. 물놀이를 가자 (SWEA 10966)

```python
from collections import deque


def bfs():
    ans = 0
    q = deque()
    for i in range(N*M):
        r, c = divmod(i, M)
        if arr[r][c] == 'W':  # L이 아닌 W를 큐에 넣음(어차피 bfs는 동시에? 이동하므로)
            q.append((r, c))
            DP[r][c] = 0

    while q:
        x, y = q.popleft()
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if (-1<nx<N) and (-1<ny<M) and DP[nx][ny] == -1:  # 방문한 적 없는 경우
                DP[nx][ny] = DP[x][y] + 1  # 이동
                ans += DP[x][y] + 1  # 결과에 +
                q.append((nx, ny))
    return ans  # 결과 반환


T = int(input())
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    DP = [[-1] * M for _ in range(N)]

    print('#{0} {1}'.format(tc, bfs()))
```

## 4. 보호필름 (SWEA 2112)

```python
def confirm(a):  # 성능검사 함수
    for col in zip(*a):  # 열 => 행
        c = 1
        val = col[0]
        for i in col[1:]:
            if i == val: c += 1
            else:
                c = 1
                val = i
            if c >= K:  # 해당 열의 검증이 된 경우
                break
        else:  # for문이 정상 종료된 것은 검증 안 된 열이 있는 것
            return False
    return True


def combination(a):  # 조합 함수
    res = []
    for i in range(0, (1<<len(a))):
        t = []
        for j in range(0, len(a)):
            if i & (1<<j):
                t.append(a[j])
        res.append(t)
    return res


def change(a):  # 변환 함수
    t = []
    for i in combination(a):  # 바꿔야 하는 행은 서로 다른 특성으로 변경 가능함
        for j in a:
            t.append(arr[j])
            if j in i: arr[j] = AB[0]  # 열 전체를 한 번에 바꿈
            else: arr[j] = AB[1]
        if confirm(arr):
            return True
    
    for i, j in enumerate(a):  # 원상 복귀
        arr[j] = t[i]
    return False


ans = []
T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    AB = [[0] * W, [1] * W]

    comb = sorted(combination([i for i in range(D)]), key=lambda x: len(x))  # 길이 기준으로 정렬해야 함
    for idx in comb:
        if change(idx):  # 답을 찾은 경우(길이가 짧은 것부터 검사함)
            ans.append('#{0} {1}'.format(tc, len(idx)))
            break

print(*ans, sep='\n')
```

## 5. 탈주범 검거 (SWEA 1953)

```python
from collections import deque


def bfs(x, y):  # 반드시 bfs 사용할 것(dfs 구현 힘듬)
    q = deque([(x, y, 1)])
    v = set([(R, C)])

    while q:
        x, y, t = q.popleft()
        
        if t == L:  # 종료 조건
            continue
    
        for i in dic1[arr[x][y]]:
            nx, ny = x + xy[i][0], y + xy[i][1]
            if (nx, ny) not in v and (-1<nx<N) and (-1<ny<M):  # 방문한 적 없고 범위 내인 경우
                if arr[nx][ny] in dic2[i]:  # 이동 가능한 경우(연결된 파이프여야 함)
                    v.add((nx, ny))
                    q.append((nx, ny, t+1))
    return len(v)

ans = []
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dic1 = {1: [0,1,2,3], 2: [0,2], 3: [1,3], 4: [0,1], 5: [1,2], 6: [2,3], 7: [0,3]}  # 파이프(key)에 따른 이동 가능한 방향 리스트(상하좌우)
dic2 = {0: (1, 2, 5, 6), 1: (1, 3, 6, 7), 2: (1, 2, 4, 7), 3: (1, 3, 4, 5)}  # 방향(key)에 따른 연결 파이프 리스트(상하좌우)
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ans.append('#{0} {1}'.format(tc, bfs(R, C)))

print(*ans, sep='\n')
```





