import sys
sys.stdin = open('input.txt')

T , d = map(int,input().split())

temperature = list(map(int,input().split()))

max_value = sum(temperature[0:d])

i = 0

if d == 1:
    print(max(temperature))
else:
    while i <= T - d:
        val = 0
        for j in range(i, i+d):
            val += temperature[j]

        if max_value < val:
            max_value = val
        i += 1

print(max_value)

