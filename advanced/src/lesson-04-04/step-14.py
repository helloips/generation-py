# https://stepik.org/lesson/416754/step/14?unit=406262

n = int(input())
matrix = list((list() for i in range(n)))

top_part = 0
right_part = 0
bottom_part = 0
left_part = 0

for row in range(n):
    matrix[row].extend(int(i) for i in input().split())

for row in range(n):
    for column in range(n):
        current_value = matrix[row][column]
        if row < column and row < n - 1 - column:
            top_part += current_value
        elif column > row > n - 1 - column:
            right_part += current_value
        elif row > column and row > n - 1 - column:
            bottom_part += current_value
        elif column < row < n - 1 - column:
            left_part += current_value

print('Верхняя четверть:', top_part)
print('Правая четверть:', right_part)
print('Нижняя четверть:', bottom_part)
print('Левая четверть:', left_part)
