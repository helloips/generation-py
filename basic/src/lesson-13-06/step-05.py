# https://stepik.org/lesson/334314/step/5?unit=317733

from math import sqrt


# объявление функции
def solve(a, b, c):
    d = b ** 2 - (4 * a * c)
    if d > 0:
        x1 = (-1 * b - sqrt(d)) / (2 * a)
        x2 = (-1 * b + sqrt(d)) / (2 * a)
        return [min(x1, x2), max(x1, x2)]
    elif d == 0:
        x = -1 * (b / (2 * a))
        return [x, x]
    else:
        return []


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
