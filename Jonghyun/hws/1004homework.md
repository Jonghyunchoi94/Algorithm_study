# 10.4 - 10.11 homework

★ **스터디 전까지 제출**

## 1. 특이한 자석 (SWEA 4013)

```python
from copy import deepcopy

def wheel(number, direction):
    if direction == 1:
        temp_data[number - 1].insert(0, temp_data[number - 1].pop())
    else:
        temp_data[number - 1].append(temp_data[number - 1].pop(0))

# 이 함수가 True이면 wheel 함수에서 움직임을 실시할 것이다.
def pair_wheel_plus_condition(number):
    if data[number - 1][6] != data[number - 2][2]:
        return True
    return False

def pair_wheel_minus_condition(number):
    if data[number - 1][2] != data[number][6]:
        return True
    return False



def change(number, direction):
    temp_plus = number + 1
    temp_minus = number - 1

    wheel(number, direction)
    direction1 = direction
    direction2 = direction

    while temp_minus >= 1:
        if pair_wheel_minus_condition(temp_minus):
            if direction1 == 1:
                wheel(temp_minus, -1)
                direction1 = -1
            else:
                wheel(temp_minus, 1)
                direction1 = 1
        else:
            break
        temp_minus -= 1

    while temp_plus <= 4:
        if pair_wheel_plus_condition(temp_plus):
            if direction2 == 1:
                wheel(temp_plus, -1)
                direction2 = -1
            else:
                wheel(temp_plus, 1)
                direction2 = 1
        else:
            break
        temp_plus += 1




T = int(input())

for case in range(T):
    K = int(input())
    data = [list(map(int, input().split())) for _ in range(4)]

    temp_data = deepcopy(data)

    for t in range(K):
        n, d = map(int, input().split())
        change(n, d)
        data = deepcopy(temp_data)

    ans = 0

    for i in range(4):
        ans += (temp_data[i][0]) * (2 ** i)

    print('#{} {}'.format(case + 1, ans))
```

## 2. 수영장 (SWEA 1952)

```python
move = [1, 1, 3]

def dfs(month, money):
    global ans, money_day
    if money >= ans:
        return

    if month > 11:
        if ans > money:
            ans = money
        return

    dfs(month + move[0], money + (data[month] * fee[0]))
    dfs(month + move[1], money + fee[1])
    dfs(month + move[2], money + fee[2])


T = int(input())

for case in range(T):
    *fee, year = list(map(int, input().split()))
    data = list(map(int, input().split()))

    ans = 987654321
    money_day = 0
    dfs(0, 0)
    print('#{} {}'.format(case + 1, min(year, ans)))
```

## 3. 가능한 시험 점수 (SWEA 3752)

```python
T = int(input())

for case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    possible_scores = [0] * (sum(data) + 1)
    possible_scores[0] = 1
    for i in data:
        for j in range(len(possible_scores)-1, -1, -1):
            if possible_scores[j] == 1:
                possible_scores[j + i] = 1

    print('#{} {}'.format(case + 1, possible_scores.count(1)))

```

## 4. 숫자 만들기 (SWEA 4008)

```python
def dfs(num, result):
    global ans_max, ans_min
    if num == N - 1:
        if ans_max < result:
            ans_max = result
        if ans_min > result:
            ans_min = result
        return

    for i in range(4):
        if cal[i]:
            cal[i] -= 1
            if i == 0:
                dfs(num + 1, result + data[num + 1])
            elif i == 1:
                dfs(num + 1, result - data[num + 1])
            elif i == 2:
                dfs(num + 1, result * data[num + 1])
            elif i == 3:
                dfs(num + 1, int(result / data[num + 1]))
            cal[i] += 1

T = int(input())

for case in range(T):
    N = int(input())
    cal = list(map(int, input().split()))
    data = list(map(int, input().split()))
    ans_max = -987654321
    ans_min = 987654321
    dfs(0, data[0])

    print('#{} {}'.format(case + 1, ans_max - ans_min))

```

## 5. 벌꿀 채취 (SWEA 2115)

```python
def pos(array1, array2):
    global honey
    global answer
    answer = []
    dfs(0, 0, 0, array1)
    max_array1 = max(answer)
    answer = []
    dfs(0, 0, 0, array2)
    max_array2 = max(answer)

    if max_array1 + max_array2 > honey:
        honey = max_array1 + max_array2

def dfs(num, result, res, arr):
    if res > C:
        return

    if num == M:
        if res <= C:
            answer.append(result)
        return

    dfs(num + 1, result, res, arr)
    dfs(num + 1, result + (arr[num] ** 2), res + arr[num], arr)


# array1, array2 구하기
def start_point(r, c):
    # 같은 행
    for i in range(c + M, N - M + 1):
        pos(data[r][c:c + M], data[r][c + M:c + (2 * M)])

    # 다른 행
    for i in range(r + 1, N):
        for j in range(N - M + 1):
            pos(data[r][c:c + M], data[i][j:j + M])

T = int(input())

for case in range(T):
    N, M, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    honey = -987654321
    for i in range(N):
        for j in range(N - M + 1):
            start_point(i, j)

    print('#{} {}'.format(case + 1, honey))
```

