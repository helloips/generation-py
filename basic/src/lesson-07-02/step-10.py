# https://stepik.org/lesson/265120/step/10?unit=246069

m, n = int(input()), int(input())

for i in range(m, n + 1):
    if i % 17 == 0 or (i % 3 == 0 and i % 5 == 0) or (i - int(i / 10) * 10) == 9:
        print(i)
