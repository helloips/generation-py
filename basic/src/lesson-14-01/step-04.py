# https://stepik.org/lesson/334152/step/4?unit=317561

# объявление функции
def draw_triangle():
    for i in range(1, 16, 2):
        print(((16 - i) // 2) * ' ', end='')
        print('*' * i)


# основная программа
draw_triangle()  # вызов функции
