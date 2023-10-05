# https://stepik.org/lesson/294243/step/8?unit=275922

n = int(input())

count = 0
for i in range(1, n + 1):
    x = (i ** 2) % 10
    if x in (2, 5, 8):
        count += i

print(count)
