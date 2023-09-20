# https://stepik.org/lesson/265081/step/6?unit=246029

number = int(input())

digit_1 = (number // 10 ** 3) % 10
digit_2 = (number // 10 ** 2) % 10
digit_3 = (number // 10 ** 1) % 10
digit_4 = (number // 10 ** 0) % 10

if (digit_1 + digit_4) == (digit_2 - digit_3):
    print('ДА')
else:
    print('НЕТ')
