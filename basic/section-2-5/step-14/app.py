# https://stepik.org/lesson/284816/step/14?unit=266160

number = int(input())
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10
print(first_digit, second_digit, third_digit, sep='')
print(first_digit, third_digit, second_digit, sep='')
print(second_digit, first_digit, third_digit, sep='')
print(second_digit, third_digit, first_digit, sep='')
print(third_digit, first_digit, second_digit, sep='')
print(third_digit, second_digit, first_digit, sep='')
