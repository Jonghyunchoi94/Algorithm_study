# 10.4 - 10.11 homework

★ **스터디 전까지 제출**

## 1. 특이한 자석 (SWEA 4013)

```python
ans = []
T = int(input())
for tc in range(1, T+1):
    K = int(input())

    res = 0
    idx = [0] * 4  # 12시 방향 인덱스
    arr = [list(map(int, input().split())) for _ in range(4)]
    
    for _ in range(K):
        a, b = map(int, input().split())

        a -= 1  # 인덱스를 맞추기 위해 -1
        t = [0] * 4  # 인덱스를 어떤 방향으로 움직일지 결정하는 리스트
        t[a] = -b
        for i in range(a, 0, -1):  # a보다 작은 방향
            if (arr[i][(idx[i]-2)%8]) != (arr[i-1][(idx[i-1]+2)%8]):  # 다른 경우
                t[i-1] = b if (a-(i-1)) % 2 else -b  # 홀수번인지 짝수번인지에 따라 방향 다르게
            else: break  # 같으면 멈춤
        
        for i in range(a, 3):  # a보다 큰 방향
            if (arr[i][(idx[i]+2)%8]) != (arr[i+1][(idx[i+1]-2)%8]):
                t[i+1] = b if ((i+1)-a) % 2 else -b
            else: break

        for i in range(4):  # 톱니바퀴 돌리기
            if t[i]:
                idx[i] = (idx[i]+t[i]) % 8  # 미리 구해둔 t[i] 값을 돌림
        
    for i in range(4):  # 최종 결과 계산
        if arr[i][idx[i]] == 1:
            res += 2**i

    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
```

## 2. 수영장 (SWEA 1952)

```python
ans = []
T = int(input())
for tc in range(1, T+1):
    C = list(map(int, input().split()))
    P = list(map(int, input().split()))

    DP = [0] * 12  # 12개월
    for i in range(12):
        if i < 2:  # 1일, 1달 이용권으로 점화식
            DP[i] = min(P[i]*C[0], C[1])+DP[i-1]
        elif i < 11:  # 1일, 1달, 3달 이용권으로 점화식
            DP[i] = min(min(P[i]*C[0], C[1])+DP[i-1], DP[i-3]+C[2])
        else:  # 모든 이용권으로 점화식
            DP[i] = min(min(P[i]*C[0], C[1])+DP[i-1], DP[i-3]+C[2], C[3])

    
    ans.append('#{0} {1}'.format(tc, DP[-1]))

print(*ans, sep='\n')
```

## 3. 가능한 시험 점수 (SWEA 3752)

```python
ans = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    v = [0]  # 방문 리스트(0은 방문)
    DP = [1] + [0] * sum(arr)  # 인덱스: 숫자, 값: 1이면 나온 값
    for i in arr:
        for j in v[:]:  # 슬라이싱으로 해야 함(for문 내에서 값이 추가되므로)
            if DP[i+j]: continue  # 이미 나온 값은 거름
            DP[i+j] = 1  # 방문 표시
            v.append(i+j)

    ans.append('#{0} {1}'.format(tc, len(v)))

print(*ans, sep='\n')
```

## 4. 숫자 만들기 (SWEA 4008)

```python
def dfs(n, a, s, m, d, v):  # 인덱스, 덧셈, 뺄셈, 곱셈, 나눗셈, 값
    global res1, res2
    if n == N:
        res1 = max(res1, v)  # 최대값
        res2 = min(res2, v)  # 최소값
        return

    if a: dfs(n+1, a-1, s, m, d, v+B[n])
    if s: dfs(n+1, a, s-1, m, d, v-B[n])
    if m: dfs(n+1, a, s, m-1, d, v*B[n])
    if d: dfs(n+1, a, s, m, d-1, int(v/B[n]))


ans = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A, B = list(map(int, input().split())), list(map(int, input().split()))

    res1, res2 = -100000000, 100000000  # 최대값, 최소값
    dfs(1, A[0], A[1], A[2], A[3], B[0])
    ans.append('#{0} {1}'.format(tc, res1-res2))

print(*ans, sep='\n')
```

## 5. 벌꿀 채취 (SWEA 2115)

```python
def adjust(arr1, arr2):  # C보다 큰 경우 조정하는 함수
    res = [0, 0]  # A 합계, B 합계
    for i in range((1<<len(arr1))):
        at, bt = 0, 0
        for j in range(len(arr1)):
            if i & (1<<j):
                at += arr1[j]
                bt += arr2[j]

        if at <= C and res[1] < bt:  # C를 만족하고 제곱합이 더 큰 경우
            res = [at, bt]
    return res


ans = []
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int ,input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [[A[i][j]**2 for j in range(N)] for i in range(N)]

    DP_A, DP_B = [[0]*(N-M+1) for _ in range(N)], [[0]*(N-M+1) for _ in range(N)]  # 각각 A, B 합계를 저장

    for i in range(N):
        for j in range(N-M+1):
            asum = sum(A[i][j:j+M])
            if asum > C: asum, bsum = adjust(A[i][j:j+M], B[i][j:j+M])  # C를 만족하지 않는 경우 조정
            else: bsum = sum(B[i][j:j+M])  # C를 만족하면 B 합계를 계산
            DP_A[i][j] = asum
            DP_B[i][j] = bsum

    res, l = 0, len(DP_A[0])
    for i in range(l*N):
        ir, ic = divmod(i, l)
        for j in range(i, l*N):
            jr, jc = divmod(j, l)
            if ir == jr:  # 같은 행인 경우
                if jc >= ic + M:  # M 이상 차이나는 경우
                    res = max(res, DP_B[ir][ic] + DP_B[jr][jc])  # 최대값 갱신
            else:  # 다른 행인 경우
                res = max(res, DP_B[ir][ic] + DP_B[jr][jc])  # 최대값 갱신

    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
```

