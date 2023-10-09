# https://stepik.org/lesson/265122/step/6?unit=246071

number = int(input())

min_digit, max_digit = 9, 0

while number != 0:
    last_digit = number % 10
    number //= 10
    if last_digit < min_digit:
        min_digit = last_digit
    if last_digit > max_digit:
        max_digit = last_digit

print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)
