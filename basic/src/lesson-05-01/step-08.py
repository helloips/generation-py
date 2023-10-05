# https://stepik.org/lesson/292172/step/8?unit=273659

x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())

if (x_2 - x_1) ** 2 == (y_2 - y_1) ** 2 or x_2 - x_1 == 0 or y_2 - y_1 == 0:
    print('YES')
else:
    print('NO')
