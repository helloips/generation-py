# https://stepik.org/lesson/294243/step/15?unit=275922

n = int(input())

pre_pre_number = 0
pre_number = 1

print(pre_number, end=" ")
for _ in range(2, n + 1):
    current_number = pre_number + pre_pre_number
    print(current_number, end=" ")
    pre_pre_number = pre_number
    pre_number = current_number
