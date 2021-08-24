import sys
sys.stdin = open('input.txt')

T , d = map(int,input().split())

temperature = list(map(int,input().split()))

i = 0
tem_sum = sum(temperature[0: d])
max_sum = tem_sum

if d == 1:
    print(max(temperature))
else:
    while True:
        tem_sum -= temperature[i]
        if i + d >= T:
            break
        tem_sum += temperature[i + d]
        if max_sum < tem_sum :
            max_sum = tem_sum
        i += 1
    print(max_sum)