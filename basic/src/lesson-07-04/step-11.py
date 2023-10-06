# https://stepik.org/lesson/265121/step/11?unit=246070

is_end = False
while not is_end:
    number = int(input())
    if number % 7 != 0:
        is_end = True
    else:
        print(number)
