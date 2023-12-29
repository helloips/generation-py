# https://stepik.org/lesson/334314/step/4?unit=317733

from math import pi


# объявление функции
def get_circle(radius):
    c = 2 * pi * radius
    s = pi * radius ** 2
    return c, s


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
