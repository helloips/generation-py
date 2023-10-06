# https://stepik.org/lesson/265121/step/13?unit=246070

count = 0

is_end = False
while not is_end:
    number = int(input())
    if 1 <= number <= 5:
        if number == 5:
            count += 1
    else:
        is_end = True

print(count)
