# https://stepik.org/lesson/265110/step/8?unit=246058

from math import pi, tan

n = int(input())
a = float(input())

s = (n * a ** 2) / (4 * tan(pi / n))

print(s)
