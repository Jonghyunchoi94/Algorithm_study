# 8.2 - 8.8 homework

★**8.8 18:00까지 제출**

## 1. 그룹 단어 체커 (BOJ 1316번 ) [구현, 문자열]

```python
N = int(input())

result = N      # 단어가 몇개가 해당하는지?

for i in range(N):
    word = input()
    
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass        # 같으면? 같네 (넘길줄 알아야)
        
        elif word[j] in word[j+1:]: # Slicing을 자유롭게
            result -= 1
            break       # 안같고, 요번 조건이 되면? 끝내면 되지 (더 볼필요가 없다.)

print(result)
```





## 2. 덩치 (BOJ 7568번) [DFS, 구현]

```python
N = int(input())

man = []

for _ in range(N):
    w, h = map(int, input().split()) # 앞으로 이용할 부분 (찢는거)
    man.append((w, h))

for i in man:
    rank = 1

    for j in man:
        if (i[0] < j[0]) & (i[1] < j[1]):
            rank += 1

    print(rank, end = ' ') # 한꺼번이 아니라 하나씩 출력을 해줘야되서 for와 줄 맞춤
```





## 3. 퇴사 (BOJ 14501번) [BFS, 다프] (?)

```python
```





## 4. 스타트와 링크 (BOJ 14889번) [BFS, 백트래킹] (?)

```python
```





## 5. 내적 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
# a = [1, 2, 3, 4]
# b = [-3, -1, 0, 2]

# 순차적으로 돌면서 곱하기

def solution(a, b):
    inner_product = 0
    for i in range(len(a)):
        inner_product += a[i] * b[i]
    return inner_product

# print(solution(a,b))

''''''
List comprehension

lambda : lambda a, b : a + b [p.166]
map : (함수, iterable) [05_data_structure I] [p.239]
    
zip : iterable & 동일한 개수로 이루어진 자료형을 묶어줌 [05_data_structure I] [P.246]
''''''
```





## 6. 3진법 뒤집기 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
# n = 45
# n = 125

# 리스트에 나머지를 담고, 인덱스를 이용해 계산

def solution(n):
    my_list = []
    while n > 0:
        my_list.append(n % 3)
        n = n // 3
    
    my_sum = 0
    for i in range(len(my_list)):
        my_sum += my_list[i] * (3 ** (len(my_list) - i - 1))

    return my_sum
    
# print(solution(n))

''''''
1. 글자에 숫자가 안더해지면, 숫자를 글자로 바꿔라...
2. int(value=0, base=10) : int(11,2) = 3 (2진수)
3. .reverse() : 고대로 역순
''''''
```





## 7. 삼각 달팽이 (프로그래머스 :  월간 코드 챌린지 시즌 1) (?)

```python

```





## 8. 재귀 호출과 BFS에 대해 탐구하고 설명하시오

### 0) Stack

- 박스 쌓기
- 선입후출, 후입선출 (append, pop)



### 1) Queue

- 선입선출 : 후입선출이랑 반대 개념 (popleft)
- form collections import **deque** : 스택 + 큐 장점 이용



### 2) 재귀함수

- Stack 구조 이용 (DFS)

- 종료 조건 명시 필수

- 반복문에 비해 더 간결

  ```python
  # 반복문
  def factorial_iterative(n):
      result = 1
      for i in range(1, n + 1):
          result *= i
      return result
  
  # 재귀
  def factorial_recursive(n):
      if n <= 1:
      	return 1
      return n * factorial_recursive(n - 1)
  ```
  



### 3) DFS (Depth-First-Search)

- 깊이 우선 탐색 알고리즘 (멀리 있는 노드 우선 탐색)
- 인접 행렬 / 인접 리스트
- Stack 구조에 기초
- 재귀 함수 이용



### 4) BFS (Breadth First Search)

- 너비 우선 탐색 알고리즘 (가까이 있는 노드 우선 탐색)
- Queue 구조에 기초
- Queue 자료구조 이용
- BFS 구현이 DFS 보다 조금 더 빠름





## 9. 보글게임 (?)

[보글게임 문제](https://algospot.com/judge/problem/read/BOGGLE)     :  이 문제는 다른 방법 말고 완전 탐색으로 푸시오 !

```python
```



