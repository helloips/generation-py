# https://stepik.org/lesson/294080/step/1?unit=275759

n = int(input())
s = 0
while n > 0:
    d = n % 10
    if d % 2 == 0:
        print(d)
        s += d
    n //= 10
print(s)
