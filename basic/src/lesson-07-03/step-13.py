# https://stepik.org/lesson/294243/step/13?unit=275922

n = int(input())
first_number = int(input())
second_number = int(input())

max_number = max(first_number, second_number)
pre_max_number = min(first_number, second_number)

for _ in range(3, n + 1):
    number = int(input())
    pre_max_number = max(pre_max_number, min(max_number, number))
    max_number = max(max_number, number)

print(max_number)
print(pre_max_number)
