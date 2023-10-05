# https://stepik.org/lesson/292172/step/7?unit=273659

x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())

if ((x_2 - x_1) ** 2 == 1 and (y_2 - y_1) ** 2 == 4) or ((x_2 - x_1) ** 2 == 4 and (y_2 - y_1) ** 2 == 1):
    print('YES')
else:
    print('NO')
