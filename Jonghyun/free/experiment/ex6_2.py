# n개의 원소 중 m개를 고르는 모든 조합을 찾는 알고리즘

# n : 전체 원소의 수
# picked : 지금까지 고른 원소들의 번호
# toPick : 더 고를 원소의 수

n = 7
picked = []
toPick = 4

visited = [0] * n
ans = 0


def pick(n, picked, toPick, s):
    global ans
    if toPick == 0:
        print(picked)
        ans += 1
        return

    for i in range(s, n):
        if visited[i] == 0:
            visited[i] = 1
            picked.append(i)
            pick(n, picked, toPick - 1, i + 1)
            picked.pop()
            visited[i] = 0
    return


print(pick(n, picked, toPick, 0))
print(ans)