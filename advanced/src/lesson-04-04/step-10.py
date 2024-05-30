# https://stepik.org/lesson/416754/step/10?unit=406262

n = int(input())
matrix = list((list() for i in range(n)))

for row in range(n):
    matrix[row].extend(int(i) for i in input().split())

matrix_sum = 0

for i in range(n):
    matrix_sum += matrix[i][i]

print(matrix_sum)
