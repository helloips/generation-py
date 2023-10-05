# https://stepik.org/lesson/265105/step/14?unit=246053

number = int(input())

digit_1 = int(number / 100)
digit_3 = int(number % 10)
digit_2 = int((number - 100 * digit_1 - digit_3) / 10)

digit_max = max(digit_1, digit_2, digit_3)
digit_min = min(digit_1, digit_2, digit_3)
digit_middle = digit_1 + digit_2 + digit_3 - digit_max - digit_min

if digit_max - digit_min == digit_middle:
    print('Число интересное')
else:
    print('Число неинтересное')
