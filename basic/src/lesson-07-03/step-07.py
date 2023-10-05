# https://stepik.org/lesson/294243/step/7?unit=275922

from math import e, log

n = int(input())

x = 1
for i in range(2, n + 1):
    x += 1 / i
result = x - log(n, e)

print(result)
