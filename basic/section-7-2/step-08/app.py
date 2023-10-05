# https://stepik.org/lesson/265120/step/8?unit=246069

m, n = int(input()), int(input())

actual_range = range(m, n + 1, 1) if m < n else range(m, n - 1, -1)
for i in actual_range:
    print(i)
