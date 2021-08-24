import sys
sys.stdin = open('input.txt')

T , d = map(int,input().split())

temperature = list(map(int,input().split()))

max_value = sum(temperature[0:d])

start = 0
end = T - d

while start != end:
    value_s = 0
    value_e = 0
    for i in range(d):
        value_s += temperature[start + i]
        value_e += temperature[end + i]
    if value_s > max_value:
        max_value = value_s
    if value_e > max_value:
        max_value = value_e
    start += 1
    end -= 1

print(max_value)


