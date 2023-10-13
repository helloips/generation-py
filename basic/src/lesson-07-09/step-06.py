# https://stepik.org/lesson/298796/step/6?unit=280623

from math import factorial

n = int(input())
factorial_n = 0

for i in range(1, n + 1):
    factorial_n += factorial(i)

print(factorial_n)
