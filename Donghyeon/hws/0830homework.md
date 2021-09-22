# 8.30 - 9.6 homework

★ **9.6 18:00까지 제출**

## 1. 기능개발 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
import sys
sys.stdin = open("input.txt")
from collections import deque
# 덱을 사용

def solution(progresses, speeds):
    answer = []                     # cnt가 들어갈 list
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        cnt = 0

        for i in range(len(progresses)):
            if progresses[i] >= 100:    # 100이상이면 그냥 아무것도 안함
                continue
            else:
                progresses[i] = progresses[i] + speeds[i]   # 100보다 작으면 speed를 하나씩 더해줌

        while progresses[0] >= 100: # 앞쪽부터 배포해야하기 때문에 index 0 값으로 함
            progresses.popleft()    
            speeds.popleft()
            cnt += 1
            
            if len(progresses) == 0:
                break

        if cnt > 0:
            answer.append(cnt)
    return answer

T = int(input())

for t in range(T):
    progresses = list(map(int, input().split()))
    speeds = list(map(int, input().split()))

    print(solution(progresses, speeds))
```

## 2. 프린터 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
def solution(priorities, location):
    answer = 0
    priorities = [(data, idx) for idx, data in enumerate(priorities)]

    while len(priorities) != 0:
        item = priorities.pop(0)

        if priorities and max(priorities)[0] > item[0]:  
            priorities.append(item)     # 작으면 뒤로 순번을 미룸
        else:
            answer += 1     # 출력이 하나 될 때마다 1씩 더해줌
            if item[1] == location:     # location의 위치와 같으면 break
                break

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))
```

## 3. 다리를 지나는 트럭 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge_weight = 0
    bridge = [0] * bridge_length

    while len(truck_weights) > 0:
        cnt += 1
        end = bridge.pop(0) # end는 이미 다리를 통과한 트럭
        bridge_weight -= end    # 이미 다리를 통과했기 때문에 end만큼 빼준다.

        if truck_weights[0] + sum(bridge) > weight: # 무게를 견딜 수 있는지 없는지 확인하기 위해
            bridge.append(0)            # 결딜수 없다면 bridge에 0을 append한다.
        else:
            bridge.append(truck_weights.pop(0)) # 견딜 수 있으면 트럭 한 대 다리 위로

    # 다리에 남은 트럭을 빼준다.
    while len(bridge) > 0:
        cnt += 1
        bridge.pop(0)

    return cnt

import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(T):
    bridge_length = int(input())
    weight = int(input())
    truck_weights = list(map(int, input().split()))

    print(solution(bridge_length, weight, truck_weights))
```

## 4. 주식 가격 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
# 스택 큐를 사용하지 않고 풀 수 있을 것 같아서 이렇게 품
# 리스트에 초당 주식 가격이 적혀있음
# 이중 for문을 이용해서 뒤의 주식 가격과 비교함
# 비교해서 크면 그냥 거기서 카운트를 끝냄

def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    return answer

import sys
sys.stdin = open("input.txt")

prices = list(map(int, input().split()))

print(solution(prices))

# 처음에는 바로 뒤의 값이 크다면 0으로 출력돼서 값이 조금 다르게 나옴
```

## 5. 입국 심사 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 이분 탐색)(런타임 에러)

```python
def solution(n, times):
    right = max(times) * n
    left = 1
    answer = 0

    answer = binary(left, right)
    return answer

# 시간을 이분 탐색하면서 적절한 시간을 찾아감
def binary(start, end):
    mid = (start + end) // 2
    count = 0
    for t in times:
        count += mid // t
        # 심사한 사람 수를 구하기 위해 총 시간에서 각각 시간을 나눔

    # count가 더 크면 시간을 줄여야하기 때문에 앞쪽으로 간다
    # count가 작으면 전부 심사를 못했기 때문에 뒷쪽으로 간다
    if count == n:
        return mid
    elif count < n:
        return binary(mid + 1, end)
    elif count > n:
        return binary(start, mid + 1)



import sys
sys.stdin = open("input.txt")

n = int(input())
times = list(map(int, input().split()))

print(solution(n, times))
```

## 6. 징검다리 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 이분 탐색)

```python
# 모든 경우의 수에 해당하는 n개의 바위를 제거한 후에
# 거리의 최대값을 구하는 방법이 가장 먼저 떠오름
# 무조건 시간초과 나올거 같다

# 이진탐색을 이용해서 .....
# 거리의 최소값 중에 가장 큰 값을 찾아간다..
```


