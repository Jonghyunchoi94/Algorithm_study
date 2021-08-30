import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,-1,1,-1,1]

for case in range(T):
    N, M = map(int, input().split())
    data = []
    for _ in range(M):
        x, y, c = list(map(int, input().split()))
        data.append([x, y, c])
    graph = [[-5]*N for _ in range(N)]
    graph[N // 2 - 1][N // 2 - 1] = 2
    graph[N // 2 - 1][N // 2] = 1
    graph[N // 2][N // 2 - 1] = 1
    graph[N // 2][N // 2] = 2

    for idx in data:
        x = idx[0]
        y = idx[1]
        val = idx[2]
        graph[x-1][y-1] = val
        for k in range(8):
            con_x = (x-1) + dx[k]
            con_y = (y-1) + dy[k]
            if 0 <= con_x < N and 0 <= con_y < N and abs(graph[con_x][con_y] - val) == 1:
                con = []
                while 0 <= con_x < N and 0 <= con_y < N and graph[con_x][con_y] != val and graph[con_x][con_y] != -5:
                    con.append([con_x, con_y])
                    con_x = con_x + dx[k]
                    con_y = con_y + dy[k]
                if 0 <= con_x < N and 0 <= con_y < N and graph[con_x][con_y] == val:
                    for i, j in con:
                        graph[i][j] = val
    cnt_black = 0
    cnt_white = 0
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 1:
                cnt_black += 1
            elif graph[r][c] == 2:
                cnt_white += 1

    print('#{} {} {}'.format(case + 1, cnt_black, cnt_white))



