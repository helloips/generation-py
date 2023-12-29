# https://stepik.org/lesson/333525/step/8?unit=316953

# объявление функции
def draw_triangle(fill, base):
    height = (base // 2) + 1
    for i in range(1, height):
        print(i * fill)
    print(height * fill)
    for i in range(height - 1, 0, -1):
        print(i * fill)


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
