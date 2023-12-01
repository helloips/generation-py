# https://stepik.org/lesson/296416/step/11?unit=278136

text = input()

count = 0
for i in text:
    if i != i.upper():
        count += 1

print(count)
