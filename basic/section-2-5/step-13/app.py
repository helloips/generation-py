# https://stepik.org/lesson/284816/step/13?unit=266160

number = int(input())
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10
print('Сумма цифр', '=', first_digit + second_digit + third_digit)
print('Произведение цифр', '=', first_digit * second_digit * third_digit)
