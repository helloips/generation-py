# https://stepik.org/lesson/311433/step/5?unit=293861

s = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s = s + n
print(s)
