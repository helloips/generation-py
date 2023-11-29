# https://stepik.org/lesson/284101/step/11?unit=265440

text = input()
has_digits = False

for i in text:
    if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        has_digits = True
        break

print("Цифра" if has_digits else "Цифр нет")
