# 8.16 - 8.22 homework

★ **8.22 24:00까지 제출**

## 1. 음양 더하기 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
def solution(absolutes, signs):
    
    for i in range(len(absolutes)):
        if not signs[i]:                    # True가 아니라면(Flas라면)
            absolutes[i] = -absolutes[i]    # 음수로!, 아니면 그대로고
    
    return sum(absolutes)                   # 다 더하면 됨

# Zip도 사용할만한...
# 입력형태 오류? True/False면 되는데... true/fals는 뭐여...
```



## 2. 약수의 개수와 덧셈 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
def solution(left, right):
    answer = 0                      	# 결과값 더할 것
    
    for i in range(left, right+1):  	# 범위 헷갈리지말자 []이걸 왜함
        yaksu_list = []             	# 약수를 다 담을 것
        for j in range(1, i+1):     	# 범위 헷갈리지말자 []이걸 왜함
            if i % j == 0:          	# 약수는 나눠서 나머지가 0
                yaksu_list.append(j)	# 약수 추가
        if len(yaksu_list) % 2 == 0:	# 약수 갯수가 짝수면
            answer += i             	# 양수
        else:                       	# 홀수면
            answer += -i            	# 음수

    return answer

# range() / [] 뇌정지 ㄴㄴ
# 제곱수는 약수가 홀수, sqrt, int한거랑 그냥 계산한거랑 같은지 비교
```



## 3. 괄호 회전하기 (프로그래머스 :  월간 코드 챌린지 시즌 2) ?

```python
def solution(s):
   
    s = list(s)
    cnt = 0

    for i in range(len(s)):
        s.append(s[0])
        s.remove(s[0])

        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            cnt += 0
        else:
            for j in range(len(s)//2):
                if s[2 * j] == '(' and s[2 * j + 1] == ')':
                    cnt += 1
                    break
                elif s[2 * j] == '{' and s[2 * j + 1] == '}':
                    cnt += 1
                    break

                elif s[2 * j] == '[' and s[2 * j + 1] == ']':
                    cnt += 1
                    break
               
    return cnt

print(solution("}]()[{"))

# 이 tc만 안됨 (tc 2번)
```



## 4. 재귀호출과 완전 탐색 복습 (8.2 과제) ??

[소풍](https://algospot.com/judge/problem/read/PICNIC)   문제 주제와 맞게 풀어 복습해 보시오.

```python
import sys
sys.stdin = open('input_04.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    
    cnt = 0

    for i in range(M):
        if len(L) < 3:
            cnt = 1
        else:
            if i < M - 1:
                bigyo = [L[2 * i], L[2 * i + 1]]
                if bigyo[0] != L[2 * (i + 1)] and bigyo[0] != L[2 * (i + 1) + 1]:
                    if bigyo[1] != L[2 * (i + 1)] and bigyo[1] != L[2 * (i + 1) + 1]:
                        cnt += 1
    
    print(cnt)
    
# 왜 안되지?
```



## 5. 재귀호출과 완전 탐색 복습 (8.2 과제) ???

[게임판 덮기](https://algospot.com/judge/problem/read/BOARDCOVER) 문제 주제와 맞게 풀어 복습해 보시오.

```python
import sys
sys.stdin = open('input_05.txt')

T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())    # 행, 열

    L = [list(map(str, input().split()))  for _ in range(H)]

    for i in range(H):
        for j in range(W):
    
    # 죄상단부터 도니까 밑에 케이스고, 돌면서
    # (0,0), (0,1), (1,0) / 끝 인덱스면 안됨(행)
    # (0,0), (0,1), (1,1) / 끝 인덱스면 안됨(행)
    # (0,0), (1,0), (1,-1)
    # (0,0), (1,0), (1,1) / 끝 인덱스면 안됨(행)
    # .을 #으로 바꿔주고 / 마지막 전 열까지만 진행
    # 다시 확인차 돌면서 다 # 이면 cnt += 1

    # 경우의 수 생각할려면, 결국 한번할때마다 4개를 다해보고, 다음으로 넘어가서 또 4개 해보고?
```

