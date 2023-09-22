# https://stepik.org/lesson/265082/step/10?unit=246030

green = 'зеленый'
red = 'красный'
black = 'черный'

number = int(input())
even = number % 2 == 0

if number == 0:
    print(green)
elif 1 <= number <= 10 or 19 <= number <= 28:
    if even:
        print(black)
    else:
        print(red)
elif 11 <= number <= 18 or 29 <= number <= 36:
    if even:
        print(red)
    else:
        print(black)
else:
    print('ошибка ввода')
