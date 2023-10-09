# https://stepik.org/lesson/265122/step/7?unit=246071

number = int(input())

last, all_sum, count, product, maximum = -1, 0, 0, 1, 0

while number != 0:
    current = number % 10

    last = current if last == -1 else last
    all_sum += current
    count += 1
    product *= current
    maximum = current if current > maximum else maximum

    number //= 10

print(all_sum)
print(count)
print(product)
print(all_sum / count)
print(current)
print(current + last)
