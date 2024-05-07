# https://stepik.org/lesson/415554/step/3?unit=405083

numbers = list(int(i) for i in input().split(' '))

result = list()
numbers_1 = numbers[0::2]
numbers_2 = numbers[1::2]

for index in range(len(numbers) // 2):
    result.append(numbers_2[index])
    result.append(numbers_1[index])

if len(numbers) % 2 != 0:
    result.append(numbers[-1])

print(*result)
