# https://stepik.org/lesson/416754/step/11?unit=406262

n = int(input())
matrix = list((list() for i in range(n)))

for row in range(n):
    matrix[row].extend(int(i) for i in input().split())

for i in range(n):
    avg = sum(matrix[i]) / len(matrix[i])
    result = len(list(element for element in matrix[i] if element > avg))
    print(result)
