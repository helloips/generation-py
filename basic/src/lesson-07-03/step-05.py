# https://stepik.org/lesson/294243/step/5?unit=275922

a, b = int(input()), int(input())
count = 0

for i in range(a, b + 1):
    x = (i ** 3) % 10
    if x == 4 or x == 9:
        count += 1

print(count)
