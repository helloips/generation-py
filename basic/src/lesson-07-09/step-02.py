# https://stepik.org/lesson/298796/step/2?unit=280623

n = int(input())
x = 0

for i in range(1, n + 1):
    for _ in range(i):
        x += 1
        print(x, end='')
    for _ in range(i - 1):
        x -= 1
        print(x, end='')
    print()
    x = 0
