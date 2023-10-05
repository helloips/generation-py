# https://stepik.org/lesson/294243/step/9?unit=275922

n = int(input())

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(factorial)
