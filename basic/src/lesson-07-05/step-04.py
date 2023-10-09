# https://stepik.org/lesson/265122/step/4?unit=246071

number = int(input())

while number != 0:
    last_digit = number % 10
    number //= 10
    print(last_digit)
