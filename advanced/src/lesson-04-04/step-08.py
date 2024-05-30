# https://stepik.org/lesson/416754/step/8?unit=406262

n = int(input())
m = int(input())
matrix = list((list() for i in range(n)))

for row in range(n):
    for column in range(m):
        matrix[row].append(input())

for row in range(n):
    for column in range(m):
        print(matrix[row][column], end=' ')
    if row < n - 1:
        print()
