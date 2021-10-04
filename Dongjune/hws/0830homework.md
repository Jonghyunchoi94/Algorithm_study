# 8.30 - 9.6 homework

## 1. 기능개발(프로그래머스 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택/큐)

```python
from collections import deque

def solution(progresses, speeds):
    answer = []
    stack = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    for i in range(len(progresses)):
        stack.append(progresses.popleft())

    while len(stack) > 0 and stack[0] < 100:    # 스택이 안비워져있고, 첫놈이 100이상이 될 떄까지
        for j in range(len(stack)):             # 모든 친구들이 1씩 증가 (하루에)
            stack[j] = stack[j] + speeds[j]

            if stack[0] >= 100 and j == len(stack) -1:  # 첫놈이 100이상이 되고, j는 끝까지 다 1증가가 되었는지 확인을 위해
                cnt = 0                                 # 몇놈인지
                for _ in range(len(stack)):             
                    if stack[0] >= 100:                 # 100 이상이면
                        cnt += 1                        # 1놈 추가
                        stack.pop(0)                    # 스택과 스피드에서 모두 제거
                        speeds.popleft()
                    else:                               # 아니면 종료
                        break
                answer.append(cnt)                      # 그동안 있던 친구들 답에 추가
                break                                   # 종료해서 while로(최종 조건으로)

    return answer

'''
같이 움직이니까 zip (다른 풀이)
n을 표현하고 싶었... days나 time 같은...
indentation이 복잡하니 주의
'''
```



## 2. 프린터(프로그래머스 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택/큐)

```python
# TC 2번 미통과 / 순서대로 출력은 할 수 있게 작성은 했는데... / 그 번호를 어떻게 찾을 수 있을라나... (enumerate? / visited?)

from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    printer = []
    wait = []
    num = priorities[location]	# 해당 숫자

    while len(priorities) > 0:
        printer.append(priorities.popleft())	# [2, 1, 3, 2]

        if len(priorities) > 0:
            for i in priorities:
                if printer[-1] < i:
                    wait.append(printer.pop())
                    break
                else:
                    pass

    if num in printer:
        return printer.index(num) + 1
    
    else:
        return len(printer) + wait.index(num) + 1
    
    # enumerate
    # 포인터??? :
```



## 3. 다리를 지나는 트럭(프로그래머스 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택/큐)

```python
# 최종 제출이 통과 못함 (시간 많이소요, 나중에... / 다른 풀이는 날라감 / 잘못된 부분 알거 같은데...)

from collections import deque

def solution(b_l, w, t_w):
    bridge = [0] * b_l      # 다리를 만들고
    bridge = deque(bridge)
    t_w_c = t_w.copy()  	# while을 위해(비교) 복사
    stack = []              # 통과친구들 담을거
    cnt = 0                 # 초 계산
    t_w = deque(t_w)        # popleft 쓰고 싶음

    while stack != t_w_c:   # 통과 전후 같을 때까지
        if len(t_w) == 0:   # 대기친구들이 비고 stack에 다 찼으면
            break           # 비었으면 끝
        bridge[0] = t_w.popleft()   # 첫칸은 첫친구가
        cnt += 1                    # 투입 +1

        while bridge[-1] == 0 and bridge.count(0) != b_l: 
            bridge.appendleft(bridge.pop())
            cnt += 1
                    
            if len(t_w) != 0 and sum(bridge) + t_w[0] <= w: # 대기가 있고, 다리친구 + 첫 대기 <= 한도이면
                bridge[0] = t_w.popleft()                   # 첫칸에 첫 대기 추가
                cnt += 1                                    # 투입 +1
            
        stack.append(bridge[-1])                    # 도착에 넣고
        bridge[-1] = 0                              # 떠난 자리는 0으로
        
    return cnt + 1  # 답이 1모잘라서 1더함

# 구조 먼저 생각해놓고 들어가는게 좋을수도!
```



## 4. 주식 가격(프로그래머스 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 스택/큐)

```python
from collections import deque

def solution(prices):
    prices = deque(prices)
    stack = []
    answer = []

    while len(prices) > 0:
        stack.append(prices.popleft())
        cnt = 0
        if len(prices) == 0:    # 다 마무리가 된 마지막 친구는
            answer.append(0)    # 0 추가
            break               # 끝
        for i in prices:        # stack(첫친구)과 1개씩 다 비교
            if stack[-1] <= i:  # 이하이면 1추가
                cnt += 1
            else:               # 큰놈이면 1추가는 하고 정지
                cnt += 1
                break
        answer.append(cnt)      # 마지막에 반영

    return answer

'''
옆 친구와의 비교 : index 범위 주의 (다른 풀이)
중도인지, 끝인지 경우에 초를 어떻게 반영하는지 주의
'''
```



## 5. 입국 심사(프로그래머스 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 이분탐색)

```python
# 최종 제출 통과 못함 (이분탐색으론... / 모두 시간초과... 이유는 알겠는데... / 이분탐색 이론은 아는데... / 문제 이해는 했음)

from itertools import permutations

def solution(n, times):
    my_list = []
    my_val = []
    min_value = 1e23 # 1e9(10 ** 9)

    for i in range(n+1):
        my_list.append(i)

    my_per = list(permutations(my_list, len(times)))
            
    for j in my_per:
        if sum(j) == n:
            my_val.append(j)

    for k in my_val:
        my_result = []
        for l in range(len(times)):
            my_result.append(list(k)[l] * times[l])
        if min_value > max(my_result):
            min_value = max(my_result)
    
    return min_value
# 이분탐색 가능하다!
```



## 6. 징검다리(프로그래머스 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 이분탐색)

```python
# 이진탐색...대부분의 풀이가 같음

def solution(distance, rocks, n):
    answer = 0
    start = 0
    end = distance
    rocks.sort()
    
    while start <= end:
        mid = (start + end) // 2
        
        # 과정이 이해가 안감(구글링)
        
        # target이 mid 보다 작으면, end = mid -1
        # target이 mid 보다 크면, star = mid + 1

    return answer


'''
def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    
    rocks.sort() #정렬되어 있지 않은 상태이기 때문에 정렬해야한다.
    
    #이분 탐색
    while start <= end: 
        mid = (start + end) // 2 #중간값을 구한다.
        del_stones = 0 #제거한 돌을 카운트하기 위한 변수
        pre_stone = 0 #기준이되는 돌(시작지점)
        for rock in rocks: #징검다리를 돌면서 
            if rock - pre_stone <  mid: #돌사이의 거리가 가정한 값보다 작으면 제거한다.
                del_stones += 1 
            else: #아니라면 그 돌을 새로운 기준으로 세운다.
                pre_stone = rock
             
            if del_stones > n: #제거된 돌이 문제 조건 보다 크면 for문을 나온다
            	break
                
        if del_stones > n: #제거된 돌이 너무 많으면 가정한 값이 큰 것이므로 범위를 작은 쪽으로 줄인다.
            end = mid - 1
        else: #반대라면 큰 쪽으로 줄인다.
            answer = mid
            start = mid + 1
            
    return answer
'''
```

