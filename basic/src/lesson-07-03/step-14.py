# https://stepik.org/lesson/294243/step/14?unit=275922

n = 10
result = True

for _ in range(n):
    number = int(input())
    if number % 2 != 0:
        result = False
        break

print('YES' if result else 'NO')
