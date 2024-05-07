# https://stepik.org/lesson/415554/step/2?unit=405083

result = 0
numbers = list(int(i) for i in input().split())

pre_last_number = numbers[0]
for i in numbers[1:]:
    if i > pre_last_number:
        result += 1
    pre_last_number = i

print(result)
