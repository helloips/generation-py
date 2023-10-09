# https://stepik.org/lesson/265122/step/9?unit=246071

number = int(input())

result = 'YES'
expected_digit = number % 10

while number != 0:
    current_digit = number % 10
    if current_digit != expected_digit:
        result = 'NO'
    number //= 10

print(result)
