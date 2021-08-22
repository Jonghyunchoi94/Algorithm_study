# 8.16 - 8.22 homework (수정 후 다시 제출 예정)

★ **8.22 18:00까지 제출**

## 1. 음양 더하기 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

absolutes = [4,7,12]
signs = [True, False, True]


print(solution(absolutes, signs))
```



## 2. 약수의 개수와 덧셈 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
def solution(left, right):
    answer = 0
    factor = []
    result = []
    for num in range(left, right+1):
        factor = []
        for i in range(1, num+1):
            if num % i == 0:
                factor.append(i)
        cnt = len(factor)

        if cnt % 2 == 1:
            num = num * (-1)
            result.append(num)
        else:
            result.append(num)

    answer += sum(result)

    return answer

print(solution(13, 17))
```



## 3. 괄호 회전하기 (프로그래머스 :  월간 코드 챌린지 시즌 2)

```python
def solution(string):
    result = []
    for n in range(len(string)):
        new_string = ['' for _ in range(len(string))]
        for i in range(len(string)):
            k = i - n
            new_string[i] = string[k]

        stack = []
        for s in new_string:
            if s == '{' or s == '(' or s == '[':
                stack.append(s)
            elif s == '}':
                if len(stack) and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(s)
            elif s == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
            elif s == ']':
                if len(stack) and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s)

        result.append(len(stack))
    return result.count(0)

string = '(){}[]'
print(solution(string))

```



## 4. 재귀호출과 완전 탐색 복습 (8.2 과제)

[소풍](https://algospot.com/judge/problem/read/PICNIC)   문제 주제와 맞게 풀어 복습해 보시오.

```python
```



## 5. 재귀호출과 완전 탐색 복습 (8.2 과제)

[게임판 덮기](https://algospot.com/judge/problem/read/BOARDCOVER) 문제 주제와 맞게 풀어 복습해 보시오.