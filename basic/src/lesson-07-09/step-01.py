# https://stepik.org/lesson/298796/step/1?unit=280623

n = int(input())
x = 1

for i in range(1, n + 1):
    for _ in range(i):
        print(x, end=' ')
        x += 1
    print()
