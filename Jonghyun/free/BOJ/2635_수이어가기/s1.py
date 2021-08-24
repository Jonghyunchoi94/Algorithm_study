import sys
sys.stdin = open('input.txt')

N = int(input())

i = N
max_res = []
max_len = 0

while i > 0:
    start = 0
    res = [N, i]
    while True:
        if start == 'err':
            break
        if res[start] - res[start + 1] >= 0:
            res.append(res[start] - res[start + 1])
            start += 1
        else:
            start = 'err'

    if len(res) > max_len:
        max_len = len(res)
        max_res = res[:]
    i -= 1
print(max_len)
print(' '.join(map(str, max_res)))



