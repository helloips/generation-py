# https://stepik.org/lesson/265121/step/12?unit=246070

result = 0

is_end = False
while not is_end:
    number = int(input())
    if number < 0:
        is_end = True
    else:
        result += number

print(result)
