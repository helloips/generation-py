# https://stepik.org/lesson/298795/step/7?unit=280622

n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()
