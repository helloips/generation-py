# https://stepik.org/lesson/298796/step/7?unit=280623

a, b = int(input()), int(input())

for i in range(a, b + 1):
    is_simple = True
    for j in range(2, i):
        if i % j == 0:
            is_simple = False
    if is_simple and i != 1:
        print(i)
