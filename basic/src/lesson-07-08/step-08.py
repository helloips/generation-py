# https://stepik.org/lesson/298795/step/8?unit=280622

n = int(input())

for i in range(1, (n + 1) // 2 + 1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(n // 2, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
