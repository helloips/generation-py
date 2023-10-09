# https://stepik.org/lesson/265122/step/5?unit=246071

number = int(input())

result_as_text = ''

while number != 0:
    last_digit = number % 10
    number //= 10
    result_as_text += str(last_digit)

print(int(result_as_text))
