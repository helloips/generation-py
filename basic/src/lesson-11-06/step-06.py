# https://stepik.org/lesson/324754/step/6?unit=307930

numbers = [int(x) for x in input().split()]

min_value = min(numbers)
max_value = max(numbers)
min_value_index = numbers.index(min_value)
max_value_index = numbers.index(max_value)
numbers[min_value_index] = max_value
numbers[max_value_index] = min_value

print(*numbers, sep=" ")
