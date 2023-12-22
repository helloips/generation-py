# https://stepik.org/lesson/324755/step/9?unit=307931

text = input()
numbers = text.split()
result = 0

for i in range(len(numbers) - 1):
    for u in (range(i + 1, len(numbers))):
        if numbers[i] == numbers[u]:
            result += 1

print(result)
