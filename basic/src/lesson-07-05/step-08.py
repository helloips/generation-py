# https://stepik.org/lesson/265122/step/8?unit=246071

number = int(input())

while number != 0:
    current_digit = number % 10

    if number // 100 == 0 and number // 10 != 0:
        print(current_digit)

    number //= 10
