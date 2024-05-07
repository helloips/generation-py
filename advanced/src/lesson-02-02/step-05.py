# https://stepik.org/lesson/415554/step/5?unit=405083

numbers = list(int(i) for i in input().split(' '))
count = 0
pre_number = -1
for number in numbers:
    if number != pre_number:
        count += 1
        pre_number = number

print(count)
