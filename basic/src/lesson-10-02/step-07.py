# https://stepik.org/lesson/313233/step/7?unit=295750

text = input()

result = ""
for i in range(len(text)):
    if i % 3 != 0:
        result += text[i]

print(result)
