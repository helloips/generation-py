# https://stepik.org/lesson/284101/step/15?unit=265440

number = int(input())
result_as_string = str()

while number > 0:
    result_as_string = str(number % 2) + result_as_string
    number //= 2

print(result_as_string)
