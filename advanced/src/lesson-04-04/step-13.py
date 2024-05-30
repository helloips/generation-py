# https://stepik.org/lesson/416754/step/13?unit=406262

n = int(input())
matrix = list((list() for i in range(n)))

for row in range(n):
    matrix[row].extend(int(i) for i in input().split())

max_value = matrix[0][0]

for row in range(n):
    for column in range(n):
        if (
                (column <= row <= n - 1 - column) or
                (column >= row >= n - 1 - column) or
                (row == column) or
                (row + column + 1 == n)
        ) and (matrix[row][column] > max_value):
            max_value = matrix[row][column]

print(max_value)
