# https://stepik.org/lesson/265120/step/9?unit=246069

m, n = int(input()), int(input())

for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)
