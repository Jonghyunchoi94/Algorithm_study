# 9.6 - 9.12 homework

★ **9.13 스터디 전까지 제출**

★ 이번 과제는 추후 일정에 따라 제출 일정이 변경될 수 있음 

## 1. K번째 수 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 정렬)

```python
def solution(array, commands):
    answer = []
    for idx in commands:
        data = array[idx[0]-1:idx[1]]
        data.sort()
        val = data[idx[2]-1]
        answer.append(val)
    return answer
```

## 2. 가장 큰 수 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 정렬)

```python
def solution(numbers):
    answer = list(map(str, numbers))                 # numbers는 0 ~ 1000 까지의 숫자
    answer.sort(key = lambda x:x*3  , reverse=True)  # 문자열을 3번 곱한다?  '3' * 3  => '333'
    return str(int(''.join(answer)))                 # 모든 숫자가 0일 때 '0000000' => '0'으로 출력하여야 한다.

```

## 3. H-Index (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 정렬)

```python
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
```

## 4. 단어 변환 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 깊이/너비 우선 탐색)

```python
global answer
def dfs(begin, target, words, visit):
    answer = 0
    stacks = [begin]
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer
        
        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:
                
                if visit[i] != 0:
                    continue
                visit[i] = 1
                stacks.append(words[i])
        answer += 1
    return answer

def solution(begin, target, words):
    if target not in words:
        return 0
    visit = [0 for i in words]
    answer = dfs(begin, target, words, visit)
    return answer
```

## 5. 여행경로 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 깊이/너비 우선 탐색)

```python
import collections
def solution(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
        
    answer = []
    
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        answer.append(a)
    dfs('ICN')
    return answer[::-1]
```

## 6. 체육복 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 탐욕법)

```python
def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    lost = set(lost)
    reserve = set(reserve)
    lost_r = lost - reserve
    reserve_r = reserve - lost
    for i in lost_r:
        if (i - 1) in reserve_r:
            answer += 1
            reserve_r.remove(i - 1)
            continue
        elif (i + 1) in reserve_r:
            answer += 1
            reserve_r.remove(i + 1)
            continue
    answer = n - (len(lost_r) - answer)
    return answer
```

## 7. 조이스틱 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 탐욕법)

```python
def solution(name):
    answer = 0
    for i in name:
        if ord(i) <= 77:
            answer += (ord(i) - 65)
        else:
            answer += (90 - ord(i) + 1)
    move = len(name) - 1
    
    for i in range(len(name)):
        n = i + 1
        while n < len(name) and name[n] == 'A':
            n += 1
        
        move = min(move, i + i + len(name) - n)

    answer += move
    
    return answer
```





