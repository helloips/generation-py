# https://stepik.org/lesson/416754/step/12?unit=406262

n = int(input())
matrix = list((list() for i in range(n)))

for row in range(n):
    matrix[row].extend(int(i) for i in input().split())

max_value = None

for row in range(n):
    for column in range(row + 1):
        if max_value is None or matrix[row][column] > max_value:
            max_value = matrix[row][column]

print(max_value)
