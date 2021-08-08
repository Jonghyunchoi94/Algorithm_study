# 8.2 - 8.8 homework

★**8.8 18:00까지 제출**

## 1. 그룹 단어 체커 (BOJ 1316번 )

```python
n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    error = 0

    for idx in range(len(word)-1):
        if word[idx] != word[idx-1]:
            new_word = word[idx+1:]
            if new_word.count(word[idx]) > 0:
                error += 1

    if error == 0:
        cnt += 1
print(cnt)            
```



## 2. 덩치 (BOJ 7568번)

```python
n = int(input())
cnt = 0
body_lists =[]

for _ in range(n):
    weight, height = map(int, input().split(" "))
    body_lists.append([weight, height])

for idx in range(0, len(body_lists)):
    cnt = 1
    for j in range(0, len(body_lists)):
        if body_lists[idx][0] < body_lists[j][0] and body_lists[idx][1] < body_lists[j][1]:
            cnt+=1
        
    print(cnt, end=" ")
```



## 3. 퇴사 (BOJ 14501번)

```python
n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]

for i in range(n):
    a,b = map(int, input().split())
    T[i] = a
    P[i] = b


result =[0 for i in range(n+1)]

for i in range(len(T)-2, -1, -1):      
    if T[i]+i <= n:       
        result[i] = max(P[i] + result[i + T[i]], result[i+1])   
    else:                
        result[i] = result[i+1]
print(result[0])
```



## 4. 스타트와 링크 (BOJ 14889번)

```python
```



## 5. 내적 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
def solution(a, b):
    answer=0

    for i in range(len(a)):
        answer += a[i]*b[i]


    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))
```



## 6. 3진법 뒤집기 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
def solution(n):
    answer = 0
    tmp_list = []
    n = int(input())

    while True:
        if n == 0:
            return tmp_list
            
        else:
            n = n // 3
            tmp_list.append(n%3)
        break
print(solution(45))
```



## 7. 삼각 달팽이 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python

def function1(n):
    answer = [[0 for j in range(1,i+1)] for i in range(1, n+1)]

    x = -1
    y = 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i%3 == 0:
                x+=1
            elif i % 3 == 1:
                y+=1
            else:
                x -= 1
                y -= 1
            
            answer[x][y] = num
            num += 1

    return sum(answer, [])


print(function1(10))

```



## 8. 재귀 호출과 완전 탐색에 대해 탐구하고 설명하시오

```bash
재귀 호출 : 
함수 내부에서 함수가 자기 자신을 다시 호출하는 것이다.
자기 자신을 계속 호출하므로 끝없이 반복한다. 그래서 함수 내부에 재귀 호출을 중단하는 명령문이 포함되어야 한다.

완전 탐색 : 
컴퓨터의 빠른 계산 능력을 이용해서 가능한 경우의 수를 하나하나 나열하며 답을 찾는 방법이다.
브루트 포스라도 불린다.
```



## 9. 보글게임

[보글게임 문제](https://algospot.com/judge/problem/read/BOGGLE)     :  이 문제는 다른 방법 말고 완전 탐색으로 푸시오 !

```python
```









