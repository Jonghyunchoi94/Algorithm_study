# 8.9 - 8.15 homework

★ **8.15 18:00까지 제출**

## 1. 이진 변환 반복하기 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
def solution(s):
    cnt = 0
    collect_zero = []
    while s != '1':
        remove_s = ''
        for i in s:
            if i == '1':
                remove_s += i
            else:
                collect_zero.append(i)                
        n = len(remove_s)
        change_s =''
        while n > 0:
            change_s = str(n%2) + change_s
            n //= 2
        
        s = change_s
        cnt += 1      
    return [cnt, len(collect_zero)]
```



## 2. 쿼드 압축 후 개수 세기 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):
        p = arr[x][y] 
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != p: 
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x, y + nn, nn)
                    comp(x + nn, y, nn)
                    comp(x + nn, y + nn, nn)
                    return

     
        answer[p] += 1

    comp(0, 0, N)
    return answer
```



## 3. 스타 수열 (프로그래머스 :  월간 코드 챌린지 시즌 1)

```python
from collections import Counter

def solution(s):
    answer = -1
    if len(s) == 1:
        return 0
    
    c = Counter(s)
    
    for k, v in c.items():
		# Time error 방지
        if c[k]*2 < answer:
            continue
            
        idx = 0
        max_value = k
        length = 0
        while idx < len(s)-1:
            if (s[idx] != max_value and s[idx+1] != max_value) or s[idx] == s[idx+1]:
                idx += 1
                continue
            
            length += 2
            idx += 2
        
        answer = max(answer, length)
        
    return answer
```



## 4. 다음의 개념에 대해 탐구하고 설명하시오.

### 4-1. 시간 복잡도의 개념에 대해 탐구하시오.

```bash
시간 복잡도는 문제를 해결하는데 걸리는 시간과 입력의 함수 관계를 가리킨다.
재귀 알고리즘과 분할 정복의 시간 복잡도를 비교하자면 재귀가 n번의 함수호출이 필요하는 것에 반해
분할 정복은 최소한 두 번에 한 번꼴로 n이 절반으로 줄어들기 때문에 재귀에 비해 호출 횟수가 훨씬 적으리란 것을 쉽게 예상할 수 있습니다.
```



### 4-2. 분할 정복에 대해 병합정렬과 퀵 정렬의 예시를 들어 설명하시오. (설명 시 시간 복잡도에 대해 필히 기입하시오.)

```bash
분할 정복은 다음 세 가지의 구성요소를 가지고 있습니다.
1. 문제를 더 작은 문제로 분할하는 과정 (divide)
2. 각 문제에 대해 구한 답을 원래 문제에 대한 답으로 병합하는 과정 (merge)
3. 더 이상 답을 분할하지 않고 곧장 풀 수 있는 매우 작은 문제 (base case)

분할 정복과 재귀 알고리즘의 차이는 더 작은 문제로 분할할 때 같은 크기의 부분 문제로 나눈다는 것입니다. 
병합 정렬 알고리즘은 주어진 수열을 가운데에서 쪼개 비슷한 크기의 수열 두 개로 만든 뒤 이들을 재귀 호출을 이용해 각각 정렬합니다. 그 후 정렬된 배열을 하나로 합침으로써 정렬된 전체 수열을 얻습니다. 
퀵 정렬 알고리즘은 병합 과정이 필요 없도록 한쪽의 배열에 포함된 수가 다른 쪽 배열의 수보다 항상 작도록 배열을 분할합니다. 이를 위해 퀵 정렬은 파티션이라고 부르는 단계를 도입하는데, 이는 배열에 있는 수 중 임의의 기준 수(pivot)를 지정한 후 기준보다 작거나 같은 숫자를 왼쪽, 더 큰 숫자를 오른쪽으로 보내는 과정입니다.
둘 다 시간복잡도는 O(nlogn) 이지만 퀵 정렬의 경우 최악의 시간 복잡도로 O(n^2)이 될 수 있습니다.
```



## 5. 쿼드 트리 뒤집기

[쿼드 트리 뒤집기 문제](https://algospot.com/judge/problem/read/QUADTREE) : 이 문제는 4번과 관련되어 푸시오.

```python
import sys
sys.stdin = open('input.txt')

def quad(tree, ind):
    let = tree[ind] 
    if let == 'w' or let == 'b':  # 하나면 뒤집는 것도 똑같음
        return let
    ind += 1  
    a=quad(tree,ind)
    ind += len(a)  # 왼쪽 위 부분 처리 후 그 부분의 인덱스 만큼 뒤로
    b=quad(tree,ind)
    ind += len(b)  
    c=quad(tree,ind)
    ind += len(c)
    d=quad(tree,ind)
    return 'x'+c+d+a+b
 
 
case = int(input())
for i in range(case):
    tree = input()
    print(quad(tree, 0)) # 0에서 시작

```

