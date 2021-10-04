# 9.27 - 10.3 homework

★ **스터디 전까지 제출**

## 1. 요리사 (SWEA 4012)

```python
'''
두 명의 손님에게 음식을 제공
두 명의 손님은 식성이 비슷, 최대한 비슷한 맛의 음식을 만들어 내야 한다.
N개의 식재료가 있다.
식재료들을 각각 (N / 2)개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)
이때, 각각의 음식을 A음식, B음식
비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분
음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다름


식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아
시너지 Sij가 발생(1 ≤ i ≤ N, 1 ≤ j ≤ N, i ≠ j)
각 음식의 맛은, 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합


식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고,
가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때,
두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고
그 최솟값을 정답으로 출력하는 프로그램을 작성

(세로축으로 i번째 위치에 있고 가로축으로 j번째 위치에 있는 값이 Sij이다.)

식재료의 수 N은 4이상 16이하의 짝수이다. (4 ≤ N ≤ 16)
시너지 Sij는 1이상 20,000이하의 정수이다. (1 ≤ Sij ≤ 20,000, i ≠ j)
i와 j가 서로 같은 경우의 Sij값은 정의되지 않는다. 입력에서는 0으로 주어진다.
'''


from pandas import DataFrame
from itertools import combinations      # 딴건 모르겠고, 조합으로 감

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())        # 반띵씩 사용(A, B)
    synergy = [list(map(int, input().split())) for _ in range(N)]
    # print(DataFrame(synergy))

    flavor_difference = 40000       # 최소 값을 구할 기준! (최대 40000 - 2)

    ingredients_num = {n for n in range(N)}     # 식재료 idx
    # print(ingredients_num)

    half_ingredient_num = combinations(ingredients_num, N//2)       # 반띵 가능 수
    # print(set(half_ingredient_num))

    # 여기서(바로 밑 for문만) 과정이 좀 길어지는데, 교집합이 없는애라는 조건을 통해서 단축 가능할란가
    for i in half_ingredient_num:
        flavor_sum_1 = 0        # 앞 친구 시너지 합
        flavor_sum_2 = 0        # 뒷 친구 시너지 합
        ingredients_1 = set(i)
        ingredients_2 = set(ingredients_num) - set(i)       # 이 과정을 위해 일단 집합으로 표현 (앞 아닌건 뒤이므로)
        # print(ingredients_1, ingredients_2)

        for j in range(len(ingredients_1) - 1):       # 완전 탐색(?) / 다 살펴보는거
            for k in range(j + 1, len(ingredients_1)):
                flavor_sum_1 += synergy[list(ingredients_1)[j]][list(ingredients_1)[k]]     # set은 순서가 없어서, list로 변환
                flavor_sum_1 += synergy[list(ingredients_1)[k]][list(ingredients_1)[j]]

                flavor_sum_2 += synergy[list(ingredients_2)[j]][list(ingredients_2)[k]]     # 뒷 친구도 앞 친구랑 판박이
                flavor_sum_2 += synergy[list(ingredients_2)[k]][list(ingredients_2)[j]]

        if flavor_difference > abs(flavor_sum_1 - flavor_sum_2):        # 최소 비교
            flavor_difference = abs(flavor_sum_1 - flavor_sum_2)

    print('#{} {}'.format(tc, flavor_difference))
    
```



## 2. 보물상자 비밀번호 (SWEA 5658)

```python
'''
각 변에 다음과 같이 16진수 숫자(0~F)가 적혀 있는 보물상자
보물 상자의 뚜껑은 시계방향으로 돌릴 수 있고, 한 번 돌릴 때마다 숫자가 시계방향으로 한 칸씩 회전

각 변에는 동일한 개수의 숫자가 있고, 시계방향 순으로 높은 자리 숫자에 해당하며 하나의 수를 나타낸다.

비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진 수로 만든 수이다.
N개의 숫자가 입력으로 주어졌을 때, 보물상자의 비밀 번호를 출력하는 프로그램을 만들어보자.
(서로 다른 회전 횟수에서 동일한 수가 중복으로 생성될 수 있다. 크기 순서를 셀 때 같은 수를 중복으로 세지 않도록 주의한다.)

N은 4의 배수이고, 8이상 28이하의 정수이다. (8 ≤ N ≤ 28)
N개의 숫자는 각각 0이상 F이하로 주어진다. (A~F는 알파벳 대문자로만 주어진다.)
K는 생성 가능한 수의 개수보다 크게 주어지지 않는다.

16진수 0~F 숫자가 공백 없이 N개 주어진다.
'''


from collections import deque       # pop은 했는데, 왼쪽에 어떻게 넣어주냐 이것말곤 없다
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    all_hex_list = []
    hex = list(input())     # 16진수 전체를 받고
    d_hex = deque(hex)      # 덱 사용

    for _ in range(N//4):
        original_hex = ''
        d_hex.appendleft(d_hex.pop())       # 오른쪽을 뽑아서 왼쪽에 넣는다
        # print(d_hex)
        for i in d_hex:
            original_hex += i               # 원래 글자형태로 다시 복구

        for i in range(N//4, N+1, N//4):        # 4면이니까, N//4씩 잘라줌
            if original_hex[(i - N//4) : i] not in all_hex_list:        # 중복은 넣어주지 말랬으니까
                all_hex_list.append(original_hex[(i - N//4) : i])       # 중복 빼고 리스트에 넣어줌!

    for i in range(len(all_hex_list)):
        all_hex_list[i] = int(all_hex_list[i], 16)      # 16진수를 10진수로!

    all_hex_list.sort(reverse=True)     # 내림차순

    print('#{} {}'.format(tc, all_hex_list[K-1]))       # K번째니까 K-1
    
```



## 3. 물놀이를 가자 (SWEA 10966) [풀이강의 有]

```python
'''
지도는 N×M크기의 격자로 표현,
위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이면 ‘W’, 땅이면 ‘L’로 표현
어떤 칸에 사람이 있으면, 그 칸의 상하좌우에 있는 칸으로 이동하는 것을 반복하여 다른 칸으로 이동할 수 있다.
단, 격자 밖으로 나가는 이동은 불가능하다.
땅으로 표현된 모든 칸에 대해서,
어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 모든 이동 횟수의 합을 출력하는 프로그램을 작성

문자열은 ‘W’또는 ‘L’로만 이루어져 있다.
모든 줄의 문자열을 모두 합쳤을 때, 적어도 하나의 ‘W’는 주어지는 것이 보장
각 테스트 케이스마다 땅으로 표현된 모든 칸에 대해서, 물인 칸으로 이동하기 위한 최소 이동 횟수의 합을 출력
'''

'''
from collections import deque

def BFS_land_to_water(idx):
    min_list = []
    Q = deque()
    Q.append(idx)
    visited = [[0] * M for _ in range(N)]
    visited[idx[0]][idx[1]] = 1

    while Q:
        position = Q.pop()

        if water_park[position[0]][position[1]] == 'W':
            min_list.append(position[2])
            continue

        for i in range(4):
            nx = position[0] + dx[i]
            ny = position[1] + dy[i]
            nm = position[2] + 1

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 1:
                visited[nx][ny] = 1
                Q.append([nx, ny, nm])

    return min(min_list)

import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 1, 0, 0]      # 상 하 좌 우
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    water_park = [list(map(str, ''.join(input()))) for _ in range(N)]
    # print(water_park)
    land_position = []

    for i in range(N):
        for j in range(M):
            if water_park[i][j] == 'L':
                land_position.append([i, j, 0])

    for i in land_position:
        result += BFS_land_to_water(i)

    print('#{} {}'.format(tc, result))

#1 9
#2 4
#3 15
'''

from collections import deque       # 큐(선입선출) 쓸려고 / 최소 / 가장 근처 / DFS는 깊숙하게, 끝까지

def BFS_water_to_land():            # 물에서 땅으로 / 땅에서 물로하니까 인생망함
    Q = deque()
    result = 0                      # 거리 뽑을 값
    for i in range(N):
        for j in range(M):
            if water_park[i][j] == 'W':     # 물인 곳의 idx 다담고 / visited로 거리계산을 위해 0으로 지정
                Q.append((i, j))            ########## 리스트하면 안되고, 튜플 하면 됨 ##########
                visited[i][j] = 0

    while Q:
        # pos = Q.popleft()                   # 왼쪽꺼를 뽑아야 먼저 뽑음
        x, y = Q.popleft()

        for i in range(4):                  # 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            # nx = pos[0] + dx[i]
            # ny = pos[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:       # 범위 / 방문유무 / 글자유무는 체크안함 (방문유무에서 걸러짐)
                Q.append((nx, ny))      # 해당하는 좌표 넣어줌                 ########## 리스트하면 안되고, 튜플 하면 됨 ##########
                visited[nx][ny] = visited[x][y] + 1
                # visited[nx][ny] = visited[pos[0]][pos[1]] + 1               # 거리계산을 위해 1씩 증가

    for i in visited:       # 거리 전부다 탐색해서 다 더해버림 : 최소 거리들의 합
        result += sum(i)

    return result

import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 1, 0, 0]      # 상 하 좌 우
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    water_park = [list(map(str, ''.join(input()))) for _ in range(N)]       # 각각 분해해서 담을려고 (DataFrame처럼)
    # print(water_park)
    visited = [[-1] * M for _ in range(N)]      # visited 이용할려고, 0말고 -1로 함

    print('#{} {}'.format(tc, BFS_water_to_land()))
    # print(visited)

#1 9
#2 4
#3 15
```



## 4. 보호필름 (SWEA 2112)

```python
'''
보호 필름의 성능을 검사하기 위해 합격기준 K라는 값을 사용한다.
충격은 보호 필름 단면의 세로 방향으로 가해지므로, 세로 방향 셀들의 특성이 중요하다.
단면의 모든 세로방향에 대해서 동일한 특성의 셀들이 K개 이상 연속적으로 있는 경우에만 성능검사를 통과

성능검사에 통과하기 위해서 약품을 사용하여야
약품은 막 별로 투입할 수 있으며 이 경우 투입하는 막의 모든 셀들은 하나의 특성으로 변경된다.
특정 막에 약품 A를 투입하면 막 내의 모든 셀들이 특성 A로 변경되며, 약품 B를 넣게 되면 특성이 모두 특성 B로 변경된다.

두께 D, 가로크기 W인 보호 필름 단면의 정보와 합격기준 K가 주어졌을 때
약품 투입 횟수를 최소로 하여 성능검사를 통과할 수 있는 방법을 찾고, 이때의 약품 투입 횟수를 출력

약품을 투입하지 않고도 성능검사를 통과하는 경우에는 0을 출력

보호 필름의 두께 D는 3이상 13이하의 정수 (3≤D≤13)
보호 필름의 가로크기 W는 1이상 20이하의 정수 (1≤W≤20)
합격기준 K는 1이상 D이하의 정수 (1≤K≤D)
셀이 가질 수 있는 특성은 A, B 두 개만 존재
'''

def check(film, cobination_num):
    global inspect

    for i in combination_num:
        if


def use_drug():
    global inspect

    D_num = [i for i in range(D)]

    for i in range(1, D+1):
        combination_num = combinations(D_num, i)
        check(film, combination_num)


from itertools import combinations
from copy import deepcopy
from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())     # D : 두께, W : 가로크기, K : 합격기준
    film = [list(map(int, input().split())) for _ in range(D)]  # A : 0, B : 1
    # print(DataFrame(film))
    inspect = 0     # 약품 미사용 : 0 / 약품 사용 : 사용 횟수

    if K == 1:      # K가 1이면 걍 통과 끝
        print('#{} {}'.format(tc, inspect))


    for i in range(W):      # 열
        inspection_list = []
        cnt = 0
        for j in range(D):      # 행 / 위에서 아래로 쭉 검사
            if len(inspection_list) == 0:
                inspection_list.append(film[j][i])      # 시작할땐 0인지 1인지 넣어주고
                cnt += 1        # K와 비교하기 위해 cnt진행
            else:
                if inspection_list[-1] == film[j][i]:   # 같으면
                    cnt += 1        # cnt +1
                    if cnt >= K:    # K이상이면 해당열은 합격
                        break       # 다음 열로 넘어감
                else:                                   # 다르면
                    inspection_list[-1] = film[j][i]    # 해당 숫자 바꿔주고
                    cnt = 1                             # 1로 다시 시작
                    if j > D-K:                         # 남은 것을 봐도 K가 안되는 위치이면
                        use_drug()                      # 약품쓰는 함수로 Go

    print('#{} {}'.format(tc, inspect))

```



## 5. 탈주범 검거 (SWEA 1953) [풀이강의 有]

```python
'''
탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,
탈주범은 시간당 1의 거리를 움직일 수 있다.
터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산

0 없을 무
1 상하좌우
2 상하
3 좌우
4 상우
5 하우
6 하좌
7 상좌

탈주범이 있을 수 있는 장소는, 맨홀뚜껑이 위치한 지점을 포함
지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소의 개수를 계산
'''

def check_available(delta):     # 주둥이가 맞는지 확인하는 함수 (그 때 가능한 친구들을 리스트로)
    if delta == (-1, 0):
        return [1, 2, 5, 6]

    elif delta == (1, 0):
        return [1, 2, 4, 7]

    elif delta == (0, -1):
        return [1, 3, 4, 5]

    else:
        return [1, 3, 6, 7]


def check_position(R, C, L):    # L만큼 DFS진행해서 찾을려고

    if L == 0:                  # 0초 되면 정지
        return

    else:
        for i in range(1, 8):   # 1~7까지 종류
            if underground_tunnel[R][C] == i:       # 1~7이면
                for j in delta_dict_xy[i]:          # 그때 가능한 델타를 진행
                    available = check_available(j)  # 가능한 주둥이는 무엇이 있는가
                    NR = R + j[0]                   # 새로운 진행방향
                    NC = C + j[1]
                    if 0 <= NR < N and 0 <= NC < M and underground_tunnel[NR][NC] in available and visited[NR][NC] == 0:    # 범위를 벗어나지 않고, 주둥이 리스트에 있고, 방문을 안했다면
                        visited[NR][NC] = 1     # 방문처리
                        check[NR][NC] = 1       # check처리 (그냥 cnt를 더하면 중복되는 경우{시간이 너무 길어서 다양하게 해당 지점에 위치할 수도 있으니까} 때문에 따로 만듬!)
                        check_position(NR, NC, L-1)     # 시간 1 줄여서 동일하게 재귀
                        visited[NR][NC] = 0     # 나오면 방문처리 복구


import sys
sys.stdin = open('input.txt')

T = int(input())

# 해당 숫자에 대해서 갈 수 있는 delta를 리스트로 받아줌, for문 돌릴려고
delta_dict_xy = {1 : [(-1, 0), (1, 0), (0, -1), (0, 1)], 2 : [(-1, 0), (1, 0)], 3 : [(0, -1), (0, 1)], 4 : [(-1, 0), (0, 1)], 5 : [(1, 0), (0, 1)], 6 : [(1, 0), (0, -1)], 7 : [(-1, 0), (0, -1)]}

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())        # 지하 터널 세로, 가로 / 맨홀 세로, 가로 / 소요시간

    underground_tunnel = [list(map(int, input().split())) for _ in range(N)]
    # print(underground_tunnel)
    cnt = 0                                         # 탈주범이 위치할 수 있는 장소 카운트
    visited = [[0] * M for _ in range(N)]           # 방문 체크
    check = [[0] * M for _ in range(N)]             # 위치하는 장소를 체크


    visited[R][C] = 1                               # 시작 지점 방문
    check[R][C] = 1                                 # 역시 시작지점 체크
    check_position(R, C, L-1)                       # 처음 시작지점에 1시간 씀

    for i in range(N):                              # 체크에 1 되있으면 다 위치할 수 있는 장소임
        for j in range(M):
            if check[i][j] == 1:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

```

