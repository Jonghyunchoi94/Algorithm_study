# 8.30 - 9.6 homework

★ **9.6 18:00까지 제출**

## 1. 기능개발 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
def solution(progresses, speeds):
    answer = []
    work = [((100 - progresses[i]) // speeds[i]) + 1 if (100 - progresses[i]) % speeds[i] else (100 - progresses[i]) // speeds[i]  for i in range(len(progresses))]
    stack = [work[0]]
    while stack:
        for i in range(1, len(work)):
            if work[i] <= stack[0]:
                stack.append(work[i])
            
            elif work[i] > stack[0]:
                answer.append(len(stack))
                stack.clear()
                stack.append(work[i])
        if stack:
            answer.append(len(stack))
            stack.clear()
        
    return answer
```

## 2. 프린터 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
def solution(priorities, location):
    answer = 1
    pos = 0
    while priorities:
        if pos == len(priorities):
            pos = 0
        
        for i in range(len(priorities)):
            if priorities[pos] < priorities[i]:
                break
        else:
            if pos == location:
                break
            else:
                priorities[pos] = -1
                answer += 1
        pos += 1
    

    return answer
```

## 3. 다리를 지나는 트럭 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
def solution(bridge_length, weight, truck_weights):
    cur_weight = 0
    time = 1
    stack = []
    pass_truck = []
    pos = 0

    while pos <= len(truck_weights):
        if pos < len(truck_weights) and len(stack) < bridge_length and cur_weight + truck_weights[pos] <= weight:
            cur_weight += truck_weights[pos]
            stack.append(truck_weights[pos])
            pos += 1
        elif len(stack) < bridge_length:
            stack.append(0)
        else:
            val = stack.pop(0)
            if val != 0:
                pass_truck.append(val)
            cur_weight -= val
            if pos < len(truck_weights) and cur_weight + truck_weights[pos] <= weight:
                stack.append(truck_weights[pos])
                cur_weight += truck_weights[pos]
                pos += 1
            else:
                stack.append(0)
        time += 1

        if pos == len(truck_weights) and len(stack) == bridge_length:
            pos += 1

    while stack:
        val = stack.pop(0)
        if val != 0:
            pass_truck.append(val)
            if len(pass_truck) == len(truck_weights):
                break
        time += 1

    return time
```

## 4. 주식 가격 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
from collections import deque
def solution(prices):
    answer=[]
    prices=deque(prices)
    while prices:
        stack=[]
        for i in prices:
            stack.append(i)
            if i < prices[0]:
                break
        answer.append(len(stack)-1)
        prices.popleft()
    return answer
```

## 5. 입국 심사 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 이분 탐색)

```python
def solution(n, times):
    answer = 0

    start = 1
    end = max(times)*n
    while start < end:
        cur = 0
        mid = (start + end) // 2

        for t in times:
            cur += (mid // t)

        if cur >= n:
            end = mid
        else:
            start = mid + 1
        
    answer = start
    return answer
```

## 6. 징검다리 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 이분 탐색)

```python
def solution(distance, rocks, n):
    answer = 0
    sort_rocks = sorted(rocks)
    sort_rocks.append(distance)
    start = 0
    end = distance

    while start <= end:
        mid = (start + end) // 2
        min_val = 987654321
        cur = 0
        rev_cnt = 0

        for rock in sort_rocks:
            pos = rock - cur
            if pos < mid:
                rev_cnt += 1
            else:
                cur = rock
                min_val = min(min_val, pos)

        if rev_cnt > n:
            end = mid - 1
        else:
            answer = min_val
            start = mid + 1
    return answer
```

