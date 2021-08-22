# 8.9 - 8.15 homework

★ **8.17 19:00까지 제출**

## **1. 이진 변환 반복하기(프로그래머스 :  월간 코드 챌린지 시즌 1)**

```python
def solution(s):
    result = []
    number_0 = 0
    cnt = 0

    while s != '1': # 상관없다구
        cnt += 1
        number_0 += list(s).count('0')
        s = s.replace('0','') # 제거한 걸 변수로 지정해줘야 된다. (S[원본]는 그대로 유지)
        after_0 = len(s)
        
        s = ''

        while after_0 > 0:
            s += str(after_0 % 2) # ?
            after_0 = after_0 // 2
            
    result.append(cnt)
    result.append(number_0)

    return result

""""""

bin(x) : x를 0b랑 이진수로변환된 숫자를 같이 반환 (ex. x = 15면, 0b1111)
    
""""""
```



## **2. 쿼드압축 후 개수 세기(프로그래머스 :  월간 코드 챌린지 시즌 1) [TC 1만 통과]**

```python
def solution(arr):
    number_0 = 0
    number_1 = 0    
    my_plist = []
    my_result = [0, 0]

    for h in range(int((len(arr) / 2) + 1)):
        if h % 2 == 0:
            my_plist.append(h)

    for i in my_plist:
        for j in my_plist:
            my_sum = 0
            my_list = []

            for k in range(len(arr) // 2):
                for l in range(len(arr) // 2):
                    my_sum += arr[i + k][j + l]
                    my_list.append(arr[i + k][j + l])
                    
            if my_sum == 0:
                number_0 += 1
            elif my_sum == len(arr):
                number_1 += 1
            else:
                for m in my_list:
                    if m == 0:
                        number_0 += 1
                    else:
                        number_1 += 1
    
    my_result[0] = number_0
    my_result[1] = number_1
    return my_result

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))

# range(len)
# (0,0) (반, 0) (0, 반) (반, 반)
# 반만큼
# 다 같으면? 1개
# 좌표로? / BFS?
```



## **3. 스타 수열(프로그래머스 :  월간 코드 챌린지 시즌 1) [TC 3만 불통과]**

```python
import random   # 모르겠는데?

def solution(a):
    my_list = []

    if len(a) < 2:  # 부분수열이 스타수열 만족 X
        return 0
    
    else:
        for i in range(1, int((len(a) // 2)) + 1):  # 짝수 배열 추출
            my_list.append(random.sample(a, 2 * i))
        
        for j in my_list:
            for k in range(int(len(j) // 2)):
                if j[2 * k] != j[(2 * k) + 1]:  # 이웃끼리 달라야 된다!
                    if j.count(j[k]) == len(j) // 2:    # 같은 숫자가 반은 있어야!
                        return len(j)
```



## 4. 다음의 개념에 대해 탐구하고 설명하시오.

### 4-1. 시간 복잡도의 개념에 대해 탐구하시오.

## 0️⃣ 복잡도

- 알고리즘의 성능을 나타내는 척도

- 1) **시간 복잡도** : 특정한 크기의 입력에 대하여 알고리즘이 얼마나 오래 걸리는지(**필요한 연산횟수**)
  2) 공간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘이 얼마나 많은 **메모리**를 차지하는지

  

- 동일한 기능을 수행하는 알고리즘이 있다면 일반적으로 복잡도가 낮을수록 좋은 알고리즘

- 시간과 공간은 Trade-off 관계(메모리를 더 많이 사용해서 시간을 비약적으로 줄이는 방법 : 메모이제이션)



- Big-O 표기법 : 시간 복잡도 표현, 가장 빠르게 증가하는 항만을 고려하는 표기법(함수의 상한만 표현)
- 코딩 테스트에선 최악의 경우에 대한 연산 횟수가 가장 중요
- 보통 계수를 무시함(빅오 표기법이 항상 절대적인 것은 아님)
- 일반적으로 연산 횟수 10억번에 통상 1초 소요

| 표기법(밑이 2)           | 명칭 [위쪽에 있을수록 더 빠름!] |
| ------------------------ | ------------------------------- |
| O(1)                     | 상수 시간(Constant time)        |
| O(logN)                  | 로그 시간(Log time)             |
| O(N)                     | 선형 시간                       |
| O(NlogN)                 | 로그 선형 시간                  |
| O(N^2)                   | 이차 시간                       |
| O(N^3) [사용하기 어려움] | 삼차 시간                       |
| O(2^n) [사용하기 어려움] | 지수 시간                       |



### 4-2. 분할 정복에 대해 병합정렬과 퀵 정렬의 예시를 들어 설명하시오. (설명 시 시간 복잡도에 대해 필히 기입하시오.)

## 1️⃣ 퀵 정렬

- 평균 시간 복잡도 : O(NlogN) / 최악의 경우엔, O(N^2)
- 다른 정렬 알고리즘에 비해 빠름
- 불안정 정렬, 즉 '이미 데이터가 정렬되어 있는 경우'에는 매우 느리게 작동(삽입 정렬과 반대)
- 방법 : pivot(맨 앞)을 정한 뒤, 왼쪽(작은)/오른쪽(큰) 분할하여 진행 → 나눈 배열들에 재귀적으로 진행

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array	# 리스트가 하나 이하의 원소만을 담고 있으면 종료
    
    pivot = array[0]	# 피벗은 첫 번째 원소
    tail = array[1:]	# 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot]	# 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]	# 분할된 오른쪽 부분
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 반환
    
print(quick_sort(array))

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```



## 2️⃣ 병합 정렬

- 평균 시간 복잡도 : O(NlogN) / 최악의 경우엔, O(NlogN)
- 다른 정렬 알고리즘에 비해 빠름
- 안정 정렬, '이미 데이터가 정렬되어 있는 경우'에는 매우 빠르게 작동
- 방법 : 요소를 쪼갬 → 정렬 → 다시 합침

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    low_array = merge_sort(array[:mid])
    high_array = merge_sort(array[mid:])

    merged_array = []
    l = h = 0
    while l < len(low_array) and h < len(high_array):
        if low_array[l] < high_array[h]:
            merged_array.append(low_array[l])
            l += 1
        else:
            merged_array.append(high_array[h])
            h += 1
    merged_array += low_array[l:]
    merged_array += high_array[h:]
    return merged_array

[0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9]
```



## 5. 쿼드 트리 뒤집기

[쿼드 트리 뒤집기 문제](https://algospot.com/judge/problem/read/QUADTREE) : 이 문제는 4번과 관련되어 푸시오.

```python
# 규칙... 그려서
# 상하로 뒤집고... 그려서
# 문제 이해 완료! (입출력은 이해함)

# 규칙은...
# X가 있을 때 없을 때?

# 마지막으로 뒤집는건?
# 분할정복...

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = list(map(str, input()))

    # 처음을 찾는 과정, x 다음이겠지 (없으면 바로가는거고)

    # x가 하나라면
    # 일단 알파벳나오면 1구역, 뒤에가 x or 알파벳이면 이제 2구역으로 넘어가는거고
    # xw x면 1구역 / xw w 여도 1구역 
    # x의 개수에 따라 다르네...

    # 그렇게 3, 4구역을 찾고
    # 1~4 각각 4개의 리스트에 담는다
    # 1-3 교환이고, 2-4교환인데
    # 중요한건 상하 뒤집으면서 바뀌는건 우야지???    

    print(?)

# 4
# w
# xbwwb
# xbwxwbbwb
# xxwwwbxwxwbbbwwxxxwwbbbwwwwbb
   
# w
# xwbbw
# xxbwwbbbw
# xxwbxwwxbbwwbwbxwbwwxwwwxbbwb
```

