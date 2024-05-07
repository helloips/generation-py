# https://stepik.org/lesson/415554/step/6?unit=405083

SUCCESS_MESSAGE = 'ДА'
ERROR_MESSAGE = 'НЕТ'


def can_be_calculate(source_number, target_result):
    for i in range(len(source_number)):
        for u in range(len(source_number)):
            if i != u and source_number[i] * source_number[u] == target_result:
                return True
    return False


numbers = list()
n = int(input())
for index in range(n):
    current_number = int(input())
    numbers.append(current_number)

result = int(input())

print(SUCCESS_MESSAGE if can_be_calculate(numbers, result) else ERROR_MESSAGE)
