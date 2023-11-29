# https://stepik.org/lesson/284101/step/12?unit=265440

text = input()
plus_count = 0
star_count = 0

for i in text:
    if i == '+':
        plus_count += 1
    elif i == '*':
        star_count += 1

print("Символ + встречается", plus_count, "раз")
print("Символ * встречается", star_count, "раз")
