# https://stepik.org/lesson/298796/step/5?unit=280623

number = int(input())

while number > 9:
    digit_sqrt = 0
    while number != 0:
        last_digit = number % 10
        number //= 10
        digit_sqrt += last_digit
    number = digit_sqrt

print(number)
