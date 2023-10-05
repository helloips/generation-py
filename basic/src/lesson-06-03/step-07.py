# https://stepik.org/lesson/265110/step/7?unit=246058

from math import sqrt

a, b, c = float(input()), float(input()), float(input())

d = b ** 2 - (4 * a * c)

if d > 0:
    x_1 = (-1 * b - sqrt(d)) / (2 * a)
    x_2 = (-1 * b + sqrt(d)) / (2 * a)
    print(min(x_1, x_2))
    print(max(x_1, x_2))
elif d == 0:
    x = -1 * (b / (2 * a))
    print(x)
else:
    print('Нет корней')
