# 9.6 - 9.12 homework

★ **9.26 18:00까지 제출**

## 1. K번째 수 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 정렬)

```python
def solution(array, commands):
    ans = []
    
    for command in commands:
        i, j, k = command
        ans.append(sorted(array[i-1:j])[k-1])  # 정렬 후 인덱스에 접근(sorted는 반환값 있음)
    
    return ans
```

## 2. 가장 큰 수 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 정렬)

```python
def solution(numbers):
    ans = ''.join(sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True))  # 3자리를 맞춰주고 비교하기
    return str(int(ans)) if ans[0] == '0' else ans # [0,0,0] 같은 특수 케이스를 처리하기
```

## 3. H-Index (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 정렬)

```python
def solution(citations):
    arr = sorted(citations)
    ans, s, e = 0, 0, len(arr)

    while e >= s:
        m = (e+s) // 2
        for i in range(len(arr)):  # 논문 탐색
            if m <= arr[i]:  # 정렬된 논문에서 처음으로 작거나 같은 경우 stop
                break
        else:  # 만약 작거나 같은 경우가 없는 경우
            e = m - 1  # e 포인터를 작게 만듬
            continue
        if len(arr) - i >= m:
            ans = m
            s = m + 1
        else:
            e = m - 1
    return ans
```

## 4. 단어 변환 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 깊이/너비 우선 탐색)

```python
def solution(begin, target, words):
    ans = 51
    
    
    def isgo(a, b):  # 알파벳이 하나 차이나는지 검사하는 함수
        t = 0
        for i, j in zip(a, b):
            if i != j: t += 1
            if t > 1:
                return False
        return True
    
    
    def dfs(w, c, v):
        nonlocal ans
        if w == target:  # base case
            if ans > c:
                ans = c
            return
        
        for word in words:
            if w != word:  # 같은 경우는 isgo 함수가 걸러주지 않음
                if word not in v and isgo(w, word):  # 방문한 적 없고 isgo가 True를 반환하는 경우
                    v.add(word)
                    dfs(word, c+1, v)  # 백트래킹
                    v.remove(word)
        
        
    dfs(begin, 0, set())        
    
    if ans == 51:  # 갱신된 적 없는 경우
        return 0
    return ans
```

## 5. 여행경로 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 깊이/너비 우선 탐색)

```python
def solution(tickets):
    ans, dic = ["ZZZZ"], {}  # 최댓값으로 설정
    for ticket in tickets:  # list -> dict로 변환(tickets)
        if dic.get(ticket[0]):  # 이미 key가 있는 경우
            dic[ticket[0]].append(ticket[1])  # value(list)에 추가
        else:
            dic[ticket[0]] = [ticket[1]]
    
    for key in dic:  # value(list) 정렬
        dic[key].sort(reverse=True)
    

    def dfs(s, c, v):
        nonlocal ans
        if c == len(tickets):
            if ans > v:  # 더 작은 경우(알파벳 순서가 더 앞인 경우)
                ans = v[:]
            return
        
        if dic.get(s):
            for i in reversed(dic[s]):  # 뒤에서부터 탐색(for문 내부에서 리스트를 변경하므로)
                v.append(i)
                dic[s].remove(i)  # 해당 i 제거(이 부분이 느려지는 부분이라 생각)
                dfs(i, c+1, v)  # 분할 정복
                dic[s].append(i)
                v.pop()
        else:  # 해당 상황에서 다음으로 갈 공항이 없는 경우
            return
    
    dfs("ICN", 0, ["ICN"])
    return ans
```

## 6. 체육복 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 탐욕법)

```python
def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)  # 교집합 제거한 집합 생성
    
    ans = n - len(lost)
    for i in lost:
        if (i-1) in reserve:
            ans += 1
            reserve.remove(i-1)  # 빌려줬으므로 제거
        elif (i+1) in reserve:
            ans += 1
            reserve.remove(i+1)
    
    return ans
```

## 7. 조이스틱 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 탐욕법)

```python
def solution(name):
    dic = {}
    name = list(name)  # 값 변경을 위해 리스트로 변경
    check = len([i for i in name if i != 'A'])  # 바꿔야 하는 문자 카운팅
    for i in range(65, 91):  # 알파벳 변경을 위한 값 미리 구하기
        dic[chr(i)] = min(i - 65, 91 - i)

    ans, s = 0, 0
    for _ in range(check):
        l, r = 0, 0
        while name[s-l] == 'A':  # 왼쪽 이동
            l += 1
        while name[s+r] == 'A':  # 오른쪽 이동(둘 중 더 적은 방향으로 움직임)
            r += 1
        
        s += (-l if l < r else r)
        ans += (l if l < r else r) + dic[name[s]]  # line18~20은 순서 바뀌면 안됨
        name[s] = 'A'
        
    return ans
```

