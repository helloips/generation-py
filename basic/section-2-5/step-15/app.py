# https://stepik.org/lesson/284816/step/15?unit=266160

number = int(input())
digit_1 = (number // 10 ** 3) % 10
digit_2 = (number // 10 ** 2) % 10
digit_3 = (number // 10 ** 1) % 10
digit_4 = (number // 10 ** 0) % 10
print('Цифра в позиции тысяч равна', digit_1)
print('Цифра в позиции сотен равна', digit_2)
print('Цифра в позиции десятков равна', digit_3)
print('Цифра в позиции единиц равна', digit_4)
