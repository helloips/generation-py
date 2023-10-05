# https://stepik.org/lesson/294243/step/11?unit=275922

n = int(input())
result = 0

for i in range(1, n + 1):
    if n % i == 0:
        result += i

print(result)
