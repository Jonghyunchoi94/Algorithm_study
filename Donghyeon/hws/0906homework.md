# 9.6 - 9.12 homework

★ **9.13 스터디 전까지 제출**

★ 이번 과제는 추후 일정에 따라 제출 일정이 변경될 수 있음 

## 1. K번째 수 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 정렬)

```python
def solution(array, commands):
  answer = []

  for i in range(len(commands)):
    # [i][0]번째부터 [i][1]까지 짜른다
    arr_list = array[commands[i][0]-1:commands[i][1]]
    arr_list.sort()

    # 3번째 숫자를 append
    answer.append(arr_list[commands[i][2]-1])

  return answer
```

## 2. 가장 큰 수 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 정렬)

```python
def solution(numbers):
    tmp=[]
    for index, num in enumerate(numbers):
        # 두자리수 세자리수 네자리수에 관계없이 맨 앞자리를 봐야하기 때문
        if num < 10:
            num = num*1111
        elif num<100:
            num=num*101
        elif num<1000:
            num=num*10+(num//100)
        tmp.append([num,index])

    # 정렬 후에 반대로 전환
    tmp.sort()
    tmp.reverse()

    answer=[]
    for i in range(len(numbers)):
        # tmp에 있는 인덱스에 맞춰서 리스트에 append
        answer.append(str(numbers[tmp[i][1]]))
    answer=''.join(answer)
    answer=int(answer)
    return str(answer)
```

## 3. H-Index (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 정렬)

```python
# 복잡하게 생각함
# 중간 지점을 찾아야한다고 생각함
# 3편이상인 경우가 3개가 된 경우를 찾아야함
# [3, 0, 6, 1, 5] -> [6,5,3,1,0]

def solution(citations):
    # [6,5,3,1,0]
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        # 인덱스가 숫자보다 커지는 딱 그 지점을 찾아야함
        if idx >= citation:
            return idx
    return len(citations)

```

## 4. 단어 변환 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 깊이/너비 우선 탐색) (테스트1 런타임에러)

```python
# begin에서 target에 따라 변환하는 것이 아닌 반대 경로로 생각해본다.

def solution(begin, target, words):
    answer = []

    # 리스트에 target이 없이면 아예 불가능
    if target not in words:
        return 0

    # 한 자만 다르면 True, 아니면 False
    def check(begin, tmp_word):
        cnt = 0
        for a, b in zip(begin, tmp_word):
            if a != b:
                cnt += 1
        return cnt == 1

    def search(target, words, change):
        for word in words:
            # check 함수 사용해서 한자만 다른지 확인 / 같으면 일단 리스트에 저장
            if word == target and check(begin, word):
                # change를 추가해서 나중에 최단거리를 구하기 위함
                answer.append(change)
            # 아직 target에 도달하지 못했을 때
            elif check(target, word):
                words.remove(target)
                # target을 현재 word로 바꾼다
                search(word, words, change + 1)

    search(target, words, 1)

    # answer의 값 중 최솟값을 반환
    return min(answer)

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
```

## 5. 여행경로 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 깊이/너비 우선 탐색)(1개 통과)

```python
def solution(tickets):
    answer = []
    answer.append(tickets[0][0])
    answer.append(tickets[0][1])
    while len(answer) != len(tickets) + 1:
        for ticket in tickets:
            if answer[-1] == ticket[0]:
                answer.append(ticket[1])

    return answer
```

## 6. 체육복 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 탐욕법)

```python
def solution(n, lost, reserve):
    # 그냥 수업을 들을 수 있는 학생 수
    answer = n - len(lost)
    # 앞 뒤로만 빌려줄 수 있기 때문에 정렬
    lost.sort()
    reserve.sort()
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수(제한사항)
    lost_reserve = set(lost) & set(reserve)
    answer += len(lost_reserve)

    # 리스트에 이미 추가했기 때문에 제거해준다
    for lr in lost_reserve:
        lost.remove(lr)
        reserve.remove(lr)

    # 도난당한 학생들 중에서
    for s_lost in lost:

        # 앞번호
        if (s_lost-1) in reserve:
            reserve.remove(s_lost-1)
            answer += 1

        # 뒷번호
        elif (s_lost+1) in reserve:
            reserve.remove(s_lost+1)
            answer += 1

    return answer

print(solution(5,[2, 4]	,[1, 3, 5]	))
```

## 7. 조이스틱 (프로그래머스 : 코딩테스트 연습 -> 코딩 테스트 고득점 Kit -> 탐욕법)

```python
# A가 아닌 곳으로 이동하기까지 왼쪽 오른족 이동 횟수 최소값
# 모든 곳에 다 방문해서 완성되면 종료?

```





