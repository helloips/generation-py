# https://stepik.org/lesson/294080/step/5?unit=275759

n = int(input())

while n > 999:
    n //= 10

print(n % 10)
