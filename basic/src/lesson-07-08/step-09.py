# https://stepik.org/lesson/298795/step/9?unit=280622

n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()
