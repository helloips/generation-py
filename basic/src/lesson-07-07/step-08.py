# https://stepik.org/lesson/311433/step/8?unit=293861

n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
