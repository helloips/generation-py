# https://stepik.org/lesson/298796/step/3?unit=280623

a, b = int(input()), int(input())
digit = 0
maximum = 0

for i in range(a, b + 1):
    current_maximum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            current_maximum += j
    if current_maximum >= maximum:
        digit = i
        maximum = current_maximum

print(digit, maximum)
