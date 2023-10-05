# https://stepik.org/lesson/265110/step/5?unit=246058

from math import cos, pi, sin, tan

x = float(input())

r = (x * pi) / 180
result = sin(r) + cos(r) + tan(r) ** 2

print(result)
