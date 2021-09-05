# 8.30 - 9.6 homework

★ **9.6 18:00까지 제출**

## 1. 기능개발 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
def solution(progresses, speeds):
    ans, temp = [], []
    
    for i in range(len(progresses)):  # 작업 일수 계산
        x = 100 - progresses[i]
        
        if (x//speeds[i]) == (x/speeds[i]):  # 나누어 떨어지는 경우
            temp.append(x // speeds[i])
        else:  # 나누어 떨어지지 않는 경우
            temp.append((x//speeds[i]) + 1)
    
    idx = 0  # 현재의 idx 기록
    for i in range(len(temp)):  # 배포 계산(progresses가 없는 경우 실행 안됨)
        if not ans:  # 값이 없는 경우(처음에만 실행됨)
            ans.append(1)
        else:
            if temp[i] <= temp[idx]:  # 작업 일수가 더 작은 경우
                ans[-1] += 1
            else:  # 더 큰 경우
                ans.append(1)  # 새로 1을 추가
                idx = i
    
    return ans
```

## 2. 프린터 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
# 방법1. 내 풀이(어지러움)
from collections import deque


def solution(priorities, location):
    ans = []
    x, l = priorities[location], len(priorities)  # 해당 값, 길이
    priorities = deque(priorities)
    
    while True:
        if location == 0:  # 목적 값이 제일 앞인 경우
            for i in range(1, l):
                if priorities[i] > x:  # 더 큰 값이 있는 경우
                    location = l - 1
                    priorities.append(priorities.popleft())  # 맨 앞을 맨 뒤로
                    break
            else:  # 목적 값이 제일 앞에 있는 경우
                ans.append(x)
                break
        else:  # 목적 값이 제일 앞이 아닌 경우
            for i in range(1, l):  # 뒤에 더 큰 값이 있는지 반복
                if priorities[i] > priorities[0]:
                    location -= 1
                    priorities.append(priorities.popleft())
                    break
            else:  # 제일 큰 값이 앞에 온 경우
                ans.append(priorities.popleft())
                location -= 1  # 목적 값 위치 -1
                l -= 1  # 전체 길이 -1
                    
    return len(ans)

# 방법2. 다른 사람 풀이
from collections import deque


def solution(priorities, location):
    queue =  deque((i,p) for i,p in enumerate(priorities))  # 인덱스, 우선순위
    answer = 0
    while True:
        cur = queue.popleft(0)
        if any(cur[1] < q[1] for q in queue):  # 하나라도 더 큰 숫자가 있으면 True 반환됨
            queue.append(cur)
        else:  # 맨 앞이 제일 큰 숫자인 경우
            answer += 1  # +1
            if cur[0] == location:
                return answer
```

## 3. 다리를 지나는 트럭 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
# 방법1. 내 방법(느림)
from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque()  # 다리 위의 트럭을 의미((시간, 무게))
    truck_weights.reverse()  # 대기중인 트럭을 의미
    
    w, t = 0, 0  # 현재 다리의 무게, 시간
    while truck_weights:  # 대기중인 트럭이 없을 때까지
        for i in range(len(q)-1, -1, -1):  # for문 내에서 pop을 해야하므로 뒤에서부터 접근
            if q[i][0] == bridge_length-1:  # 이번에 시간이 증가하면 도착하는 경우
                w -= q[i][1]
                q.pop()  # pop
            else:
                q[i][0] += 1  # 아니면 시간만 +1
        
        x = truck_weights.pop()
        if w + x <= weight:  # 다리 위 트럭 무게 + 진입할 트럭의 무게 <= 허용 무게
            w += x
            q.appendleft([0, x])  # [시간, 무게]를 의미(위에서 값 변경하므로 튜플 안됨 // 앞으로 추가함)
        else:
            truck_weights.append(x)  # 아닌 경우는 다시 재자리
        t += 1  # 시간 증가
    t += bridge_length  # 마지막 트럭이 다리 위에 올라간 것이므로 다리 길이만큼 +

    return t

# 방법2. 다른 사람 풀이(빠름)
from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque(0 for _ in range(bridge_length))  # 다리를 구현(각 숫자는 무게 초기는 0)
    truck_weights.reverse()  # 대기중인 트럭을 의미
    
    w, t = 0, 0  # 현재 다리의 무게, 시간
    while truck_weights:
        w -= q.popleft()  # 
        if w + truck_weights[-1] <= weight:  # 다리에 진입 가능한 경우
            w += truck_weights[-1]
            q.append(truck_weights.pop())
        else:  # 다리 진입이 불가능한 경우
            q.append(0)  # 무게 0을 추가
        t += 1
    t += bridge_length  # 마지막 트럭이 다리 위에 올라간 것이므로 다리 길이만큼 +

    return t
```

## 4. 주식 가격 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택 / 큐)

```python
# 방법1. 내 풀이(느림)
def solution(prices):
    l = len(prices)
    ans = [0] * l
    c = [0] * 10001  # 인덱스 숫자의 값보다 작은 인덱스를 저장
        
    for i in range(l):
        x = prices[i]
        
        if i >= c[x]:  # 해당 인덱스보다 작은 인덱스 번호 보다 내 인덱스 번호가 큰 경우
            for j in range(i+1, l):  # 더 작은 값 찾기
                if x > prices[j]:
                    c[x] = j
                    ans[i] = j - i
                    break
            else:  # 만약 못 찾았으면 길이를 이용
                c[x] = l - 1
                ans[i] = c[x] - i
        else:  # 나와 같은 값의 인덱스에 값이 나의 인덱스보다 작은 경우
            ans[i] = c[prices[i]] - i
    return ans

# 방법2. 다른 사람 풀이(빠름)
def solution(prices):
    stack = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:  # 스택이 있고 스택 마지막 값보다 배열의 값이 작은 경우 반복
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])  # 현재 값 push

    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
```

## 5. 입국 심사 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 이분 탐색)

```python
def solution(n, times):
    l, r = 1, max(times) * n  # l = 가장 작은 값, r = 가장 큰 값
    
    while l < r:  # 이분 탐색
        m = (l+r) // 2
        s = 0  # 배정 받은 사람의 수
        
        for t in times:  # 시간 반복
            s += m // t  # 
        
        if s >= n:  # 배정 받은 사람이 더 많거나 같은 경우
            r = m  # 최대 시간을 시간을 줄여보기
        else:  # 배정 받은 사람이 더 적은 경우
            l = m + 1  # 최소 시간을 늘려보기
    
    return l  # 최소 시간을 반환
```

## 6. 징검다리 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 이분 탐색)

```python
```

