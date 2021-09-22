import sys
sys.stdin = open('input.txt')


N = int(input())
data = list(map(int, input().split()))
data_cal = list(map(int, input().split()))
cal = []
for i, j in enumerate(data_cal):
    if i == 0:
        cal.extend(['+']*j)
    elif i == 1:
        cal.extend(['-']*j)
    elif i == 2:
        cal.extend(['*']*j)
    else:
        cal.extend(['/']*j)
max_val = -987654321
min_val = 987654321

def dfs(n, sum_res):
    global max_val, min_val

    if n == N:
        if sum_res > max_val:
            max_val = sum_res

        if sum_res < min_val:
            min_val = sum_res
        return
    else:
        if cal[n] == '+':
            dfs(n+1, sum_res + data[n])
            dfs(n+1, sum_res - data[n])
        elif cal[n] == '-':
            dfs(n+1, sum_res - data[n])
            dfs(n+1, sum_res + data[n])
        elif cal[n] == '*':
            dfs(n+1, sum_res * data[n])
            dfs(n+1, sum_res / data[n])
        elif cal[n] == '/':
            dfs(n+1, sum_res / data[n])
            dfs(n+1, sum_res * data[n])
dfs(0, 0)
print(max_val)
print(min_val)



1