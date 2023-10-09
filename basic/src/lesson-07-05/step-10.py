# https://stepik.org/lesson/265122/step/10?unit=246071

number = int(input())

result = 'YES'
pre_current_digit = 0

while number != 0:
    current_digit = number % 10
    if current_digit < pre_current_digit:
        result = 'NO'
    pre_current_digit = current_digit
    number //= 10

print(result)
