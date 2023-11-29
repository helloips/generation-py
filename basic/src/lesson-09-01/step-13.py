# https://stepik.org/lesson/284101/step/13?unit=265440

text = input()
count = 0

for i in range(0, len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1

print(count)
